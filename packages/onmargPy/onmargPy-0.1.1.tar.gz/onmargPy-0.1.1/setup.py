from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.1.1"
DESCRIPTION = "Python package implementing functions from the onmaRg package for R"
LONG_DESCRIPTION = "A package that loads data from the Ontario Marginalization Index into a Pandas table, and can join the data with geographic files"

# Setting up
setup(
      name="onmargPy",
      version=VERSION,
      author="William Conley",
      author_email="<william@cconley.ca>",
      description=DESCRIPTION,
      long_description_content_type="text/markdown",
      long_description=LONG_DESCRIPTION,
      packages=find_packages(),
      install_requires=[
          "pandas",
          "geopandas",
          "os",
          "re",
          "zipfile",
          "tempfile",
          "urllib",
          "io"
      ],
      keywords=[
          "python",
          "data",
          "onmarg",
          "Ontario Marginalization Index",
          "Public Health Ontario"
      ],
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows"
      ]
)