import setuptools
from pathlib import Path

setuptools.setup(name="MehdiPrinter", version="1.0", long_description=Path("README.md").read_text(), packages=["tests", "data"])