import setuptools
from pathlib import Path

setuptools.setup(
    name = "RoshaniPDF",
    version=1.0,
    long_description = Path("README.md").read_text(),
    # find_package method discover the project and find packages if any.
    packages=setuptools.find_packages(exclude = ["tests", "data"])
)

#execution of setup file -->  python setup.py sdist bdist_wheel
#sdist- for source distribution
#bdist_wheel - build distribution
