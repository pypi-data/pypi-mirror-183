from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hari_cal',
    version='0.0.1',
    description='Basic math',
    author= 'Phani Siginamsetty',
    # url = 'https://github.com/funnyPhani/Test_repo_rlms',
    # long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["OPeration in math"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['hari_cal'],
    package_dir={'':'src'},
    install_requires = [
       "pandas"
    ]
)
