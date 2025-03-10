from setuptools import setup, find_packages

setup(
    name="pypi-demo",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Your Name",
    author_email="you@example.com",
    description="A sample PyPI package for JFrog Artifactory",
    url="https://example.com",
)
