import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ddr-clips", # DDR-CLIPs runtime
    version="1.0.02", #Initial release under ddr-home
    author="Peter Van Horne",
    author_email="petervh@cisco.com",
    description="Distributed Device Reasoning (DDR) CLIPs runtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://wwwin-github.cisco.com/petervh/ddr-clips",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
                     ],
    python_requires='>=3.6',
    py_modules=['ddrrun-xr', 'ddrrun-xe', 'genie_parsers', 'ddrclass', 'ddrparserlib'],
    )
