import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vg-electricity",
    version="0.0.2",
    author="ardevd",
    author_email="5gk633atf@relay.firefox.com",
    description="Wrapper for the VG Electricity Price API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ardevd/vg-electricity",
    py_modules=['vgelectricity'],
    install_requires=[
        'aiohttp'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Development Status :: 2 - Pre-Alpha",
    ],
)
