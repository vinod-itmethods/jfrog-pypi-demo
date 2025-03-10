from setuptools import setup, find_packages

setup(
    name="demo_pypi_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Your Name",
    description="Demo package for JFrog PyPI repo",
    license="MIT"
)
