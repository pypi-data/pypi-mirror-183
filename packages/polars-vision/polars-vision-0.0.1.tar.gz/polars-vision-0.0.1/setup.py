from setuptools import setup, find_packages

packages = find_packages()
setup(
    name="polars-vision",
    packages=packages,
    include_package_data=True,
    install_requires=["polars", "pillow", "fsspec"],
    version="0.0.1",
    url="https://www.xdss.io",
    description="Vision extension for polars",
    author="Yonatan Alexander",
    author_email="jonathan@xdss.io",
    python_requires='>=3.7',
)
