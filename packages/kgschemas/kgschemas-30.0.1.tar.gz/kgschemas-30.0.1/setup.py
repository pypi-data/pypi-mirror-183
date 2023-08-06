from setuptools import setup, find_packages
import sys

import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

#number_of_arguments = len(sys.argv)
#version_parameter = sys.argv[-1]
#version = version_parameter.split("=")[1]
#sys.argv = sys.argv[0 : number_of_arguments - 1]

setup(
    name="kgschemas",
    version="30.0.1",
    description="Knowledge Graph Schemas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["pydantic"],
    packages=find_packages(),
    keywords=[],
    author="Dominic Stevenson",
    author_email="dstev@equinor.com",
)
