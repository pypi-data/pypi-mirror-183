import setuptools
from pathlib import Path
setuptools.setup(
    name = "RamkrishanPDF",
    version=1.0,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_namespace_packages(exclude=["test", "data"])
)

#python setup.py sdist{source dit} bdist_wheel {Build ditri}
#twine update dist/*