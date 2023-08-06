import ast
from setuptools import setup, find_packages


def _get_version():
    """
    Fetches the version number from the package's __init__.py file
    """
    with open("Lib/ot/__init__.py", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return ast.parse(line).body[0].value.s
        raise RuntimeError("No __version__ string found!")


with open("readme.md", "r") as f:
    long_description = f.read()

setup(
    version=_get_version(),
    package_dir={"": "Lib"},
    packages=find_packages("Lib"),
    package_data={"": ["cpg/data.txt"]},
)
