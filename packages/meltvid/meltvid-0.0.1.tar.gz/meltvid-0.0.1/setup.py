import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meltvid",
    version="0.0.1",
    author="Jonas Briguet",
    author_email="briguetjo@yahoo.de",
    description="Video editing using MLT with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Joemgu7/melt_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    keywords='video editing',
)
