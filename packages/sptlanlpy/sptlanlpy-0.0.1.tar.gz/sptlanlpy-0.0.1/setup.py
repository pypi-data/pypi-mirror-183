from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Streamlining Spatial Analyses of Cicular Data Set of Properties'
LONG_DESCRIPTION = 'A package that allows the user to conduct a SPATIAL ALALYSIS of properties surrounding a central data point within a defined radius to find trends in property value'

# Setting up
setup(
    name="sptlanlpy",
    version=VERSION,
    author="jbrinkm (Jacob Brinkmann)",
    author_email="<jbrinkm@umich.edu>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['geopy', 'geopandas', 'haversine'],
    keywords=['python', 'spatial', 'alalysis', 'MSCG', 'stadium', 'Michigan Sports Consulting Group'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Other Audience", 
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)