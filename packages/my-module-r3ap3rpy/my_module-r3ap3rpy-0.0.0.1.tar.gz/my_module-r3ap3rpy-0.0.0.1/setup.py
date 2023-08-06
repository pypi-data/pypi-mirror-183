import setuptools
import my_module

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_module-r3ap3rpy",
    version=my_module.__version__,
    author="Szabó Dániel Ernő",
    author_email="r3ap3rpy@gmail.com",
    description="A simple pypi demo package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r3ap3rpy",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)