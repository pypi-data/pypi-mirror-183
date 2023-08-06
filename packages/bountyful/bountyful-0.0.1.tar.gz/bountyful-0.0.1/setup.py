import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bountyful",
    version="0.0.1",
    author="Gianluca Truda",
    author_email="gianluca@bountyful.ai",
    description="Bountyful API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bountyful.ai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)