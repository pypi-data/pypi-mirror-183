from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(
    name="numpy_ops1234567890",
    description="A simple package to do numpy power operation",
    author="Rahul Jha",
    version="1.0.0",
    install_requires = ["numpy"],
    packages=["numpy_ops1234567890"],
    license="BSD",
    long_description=read("README.md"),
    long_description_content_type="text/markdown"
)