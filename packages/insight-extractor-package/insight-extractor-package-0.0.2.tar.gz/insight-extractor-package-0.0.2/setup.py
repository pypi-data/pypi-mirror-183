import setuptools

with open("README_PACKAGE.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="insight-extractor-package",
    version="0.0.2",
    author="Research and Innovation",
    author_email="insightextractor.dataanalytics@gmail.com",
    credits=['Renan Santos'],
    keywords='insight extractor',
    description="Insight Extractor Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
