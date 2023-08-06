from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Python Utilities grouped together.'
LONG_DESCRIPTION = 'A package that has a lot of daily use python functions/ operations.'

# Setting up
setup(
    name="arunpyutils",
    version=VERSION,
    author="Arun Kishore Voleti",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['sympy'],
    keywords=['python', 'utility'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)