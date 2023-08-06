from fsspec import AbstractFileSystem, get_filesystem_class
from fsspec.implementations.cached import SimpleCacheFileSystem
import polars as pl
import ntpath


def get_filesystem(protocol: str, **kwargs) -> AbstractFileSystem:
    klass = get_filesystem_class(protocol)
    fs = klass(**kwargs)
    return fs


def get_protocol_from_path(path: str, **kwargs) -> str:
    split = path.split(":")
    assert len(split) <= 2, f"too many colons found in {path}"
    protocol = split[0] if len(split) == 2 else "file"
    return protocol


def get_filesystem_from_path(path: str, cache_location=None, **kwargs) -> AbstractFileSystem:
    protocol = get_protocol_from_path(path)
    fs = get_filesystem(protocol, **kwargs)

    # If a cache location is set and the protocol is not a local file, use as a simple disk-based cache
    if protocol != "file" and cache_location is not None:
        fs = SimpleCacheFileSystem(fs=fs, cache_storage=str(cache_location / "simple-cache-file-system"))
    return fs


def from_files(path: str, column_name: str = 'image', cache_location: str = None,lazy:bool=False, **kwargs):
    import polars_vision as pv
    fs = get_filesystem_from_path(path, cache_location=cache_location, **kwargs)
    file_details = fs.glob(path, detail=True)
    files = [{'name': ntpath.basename(f.get('name')), column_name: f} for f in file_details.values()]
    data = pl.from_dicts(files)
    data = data.with_columns([pl.col('image').vision.to_image()])
    if lazy is False:
        data = data.with_columns([pl.col('image').vision.collect()])

    return data
