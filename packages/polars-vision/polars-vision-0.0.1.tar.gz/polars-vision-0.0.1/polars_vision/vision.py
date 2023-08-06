import numpy as np
import PIL.Image
import io
import base64
import polars as pl
import ntpath
from collections import defaultdict
import typing
from polars._html import NotebookFormatter, Tag
import html
import os

from polars_vision.filesystem import get_filesystem_from_path

THUMBNAIL_SHAPE = (150, 150)
PIL_RESAMPLING = PIL.Image.Resampling.LANCZOS


@pl.api.register_dataframe_namespace("vision")
class DataFrameVisionAccessor:
    THUMBNAIL_BYTES = 'thumbnail_bytes'
    IMAGE_BYTES = 'image_bytes'
    METADATA = 'metadata'
    URI = 'uri'
    NAME = 'name'
    SIZE = 'size'

    def __init__(self, df: pl.DataFrame):
        self._df = df

    def get_image_columns(self):
        colums = []
        for column in self._df.columns:
            value = self._df.drop_nulls(subset=[column]).head(1).to_dicts()[0][column]
            if self._validate_image_value(value):
                colums.append(column)
        return colums

    @staticmethod
    def _validate_image_value(value):
        return isinstance(value,
                          dict) and DataFrameVisionAccessor.METADATA in value and DataFrameVisionAccessor.URI in value

    @staticmethod
    def _pil2bytes(image, use_base64=True, format='png'):
        f = io.BytesIO()
        image.save(f, format)
        image_bytes = f.getvalue()
        if use_base64:
            image_bytes = base64.b64encode(image_bytes).decode('utf-8')
        return image_bytes

    @staticmethod
    def get_image_bytes(path: str):
        return get_filesystem_from_path(path).open(path).read()

    @classmethod
    def _get_thumbnail_bytes(cls, x):
        if DataFrameVisionAccessor.THUMBNAIL_BYTES in x:
            return x.get(DataFrameVisionAccessor.THUMBNAIL_BYTES)
        image_bytes = x.get(
            DataFrameVisionAccessor.IMAGE_BYTES) if DataFrameVisionAccessor.IMAGE_BYTES in x else cls.get_image_bytes(
            x.get(DataFrameVisionAccessor.URI))
        image = cls._to_pil_image(image_bytes)
        image.thumbnail(THUMBNAIL_SHAPE, PIL_RESAMPLING)
        return cls._pil2bytes(image, use_base64=True)

    @classmethod
    def get_thumbnail_html(cls, x):
        im = cls._get_thumbnail_bytes(x)
        return f'<img src="data:image/jpeg;base64,{im}">'

    @staticmethod
    def _to_pil_image(image_bytes):
        return PIL.Image.open(io.BytesIO(image_bytes))

    @staticmethod
    def _is_image_column(val, dtype):
        return dtype in (pl.Struct, pl.Object) and DataFrameVisionAccessor._validate_image_value(val)

    @classmethod
    def get_fmt_py(cls, s: pl.polars.PySeries, index: int, str_lengths: int):
        val, dtype = s.get_idx(index), s.dtype()
        if cls._is_image_column(val, dtype):
            return cls.get_thumbnail_html(val)

        ret = val
        if dtype in (pl.datatypes.Categorical, pl.datatypes.Utf8):
            val_str = str(val)[:str_lengths - 1]
            if val_str == val:
                ret = val
            else:
                ret = f"\"{val_str}..."
        return html.escape(str(ret))

    def _get_head_tail(self, max_rows=25):
        return self._df if len(self._df) <= max_rows else pl.concat(
            [self._df.head((max_rows + 1) // 2), self._df.tail((max_rows + 1) // 2)])

    def repr_html(self, **kwargs: typing.Any) -> str:
        """
        Format output data in HTML for display in Jupyter Notebooks.
        Output rows and columns can be modified by setting the following ENVIRONMENT
        variables:
        * POLARS_FMT_MAX_COLS: set the number of columns
        * POLARS_FMT_MAX_ROWS: set the number of rows

        Notes: overide the polars in case it is an html image
        """
        max_cols = int(os.environ.get("POLARS_FMT_MAX_COLS", default=75))
        if max_cols < 0:
            max_cols = self.shape[1]
        max_rows = int(os.environ.get("POLARS_FMT_MAX_ROWS", default=25))
        if max_rows < 0:
            max_rows = self.shape[0]

        from_series = kwargs.get("from_series", False)
        formatter = NotebookFormatter(
            self,
            max_cols=max_cols,
            max_rows=max_rows,
            from_series=from_series,
        )

        def write_body() -> None:
            """Write the body of an HTML table."""
            str_lengths = int(os.environ.get("POLARS_FMT_STR_LEN", "15"))
            with Tag(formatter.elements, "tbody"):
                for r in formatter.row_idx:
                    with Tag(formatter.elements, "tr"):
                        for c in formatter.col_idx:
                            with Tag(formatter.elements, "td"):
                                if r == -1 or c == -1:
                                    formatter.elements.append("...")
                                else:
                                    series = formatter.df[:, c]
                                    formatter.elements.append(
                                        DataFrameVisionAccessor.get_fmt_py(series._s, r, str_lengths))

        formatter.write_body = write_body
        return "\n".join(formatter.render())


@pl.api.register_expr_namespace("vision")
@pl.api.register_series_namespace("vision")
class ColumnVisionAccesor:
    THUMBNAIL_BYTES = 'thumbnail_bytes'
    IMAGE_BYTES = 'image_bytes'

    def __init__(self, s: pl.Series):
        self._s = s
        self.models = {}
        self.mappings = defaultdict(dict)

    @property
    def size(self):

        def _size(x):
            if isinstance(x, dict):
                return x.get(DataFrameVisionAccessor.METADATA, {}).get(DataFrameVisionAccessor.SIZE, -1)
            return -1

        return self._s.apply(_size, return_dtype=pl.Int32)

    @property
    def uri(self):
        return self._s.apply(lambda x: x.get(DataFrameVisionAccessor.URI, ''), return_dtype=pl.Utf8)

    @property
    def name(self):
        return self._s.apply(lambda x: x.get(DataFrameVisionAccessor.NAME, ''), return_dtype=pl.Utf8)

    @property
    def shape(self):

        def _shape(x):
            return self._to_numpy(x).shape

        return self._s.apply(_shape)

    @property
    def metadata(self, ):
        return self._s.apply(lambda x: x.get(DataFrameVisionAccessor.METADATA, {}))

    @staticmethod
    def _bytes2numpy(b):
        return np.array(PIL.Image.open(io.BytesIO(b)))

    @staticmethod
    def _pil2bytes(image, use_base64=False, format='png'):
        f = io.BytesIO()
        image.save(f, format)
        image_bytes = f.getvalue()
        if use_base64:
            image_bytes = base64.b64encode(image_bytes).decode('utf-8')
        return image_bytes

    @staticmethod
    def _bytes2pil(b, use_base64=False):
        if use_base64:
            b = base64.b64decode(b)
        return PIL.Image.open(io.BytesIO(b))

    @staticmethod
    def _to_pil_image(image_bytes):
        return PIL.Image.open(io.BytesIO(image_bytes))

    @staticmethod
    def _get_image_bytes(x):
        return x.get(
            DataFrameVisionAccessor.IMAGE_BYTES) if DataFrameVisionAccessor.IMAGE_BYTES in x else DataFrameVisionAccessor.get_image_bytes(
            x.get(DataFrameVisionAccessor.URI))

    def _to_image_dict(self, struct):
        uri = struct.pop('name')
        name = ntpath.basename(uri)
        struct[DataFrameVisionAccessor.URI] = uri
        struct[DataFrameVisionAccessor.NAME] = name
        return {DataFrameVisionAccessor.METADATA: struct.copy(), DataFrameVisionAccessor.NAME: name,
                DataFrameVisionAccessor.URI: uri}

    def _to_numpy(self, x):
        return self._bytes2numpy(self._get_image_bytes(x))

    def _collect(self, x):
        x[DataFrameVisionAccessor.IMAGE_BYTES] = self._get_image_bytes(x)
        return x

    def to_image(self, column_name='image'):
        return self._s.apply(self._to_image_dict).alias(column_name)

    def to_numpy(self):
        return self._s.apply(self._to_numpy)

    def to_pil(self):
        def _to_pil(x):
            return self._bytes2pil(self._get_image_bytes(x))
        return self._s.apply(_to_pil)

    def collect(self):
        return self._s.apply(self._collect)

    def thumbnails(self):
        pass  # TODO


pl.DataFrame._repr_html_ = DataFrameVisionAccessor.repr_html
# https://github.com/ethereon/lycon