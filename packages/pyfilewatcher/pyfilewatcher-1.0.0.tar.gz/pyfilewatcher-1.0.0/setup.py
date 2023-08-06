import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfilewatcher",
    version="1.0.0",
    author="Smartizer",
    author_email="info@smartizer.io",
    description="A library for monitoring files and directories for changes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bbenouarets/pyfilewatcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
