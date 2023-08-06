import setuptools
from pathlib import Path


# setupfile
setuptools.setup(
    name="zainpdf_ivan",
    version=1.7,
    long_description=Path("README.md").read_text(),
    # provide list of packages you want to ignore during finding
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
 