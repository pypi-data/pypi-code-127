from os.path import abspath, dirname

from setuptools import setup

LONG_DESCRIPTION = open(dirname(abspath(__file__)) + "/README.md", "r").read()


setup(
    name="mypy-boto3-nimble",
    version="1.24.30",
    packages=["mypy_boto3_nimble"],
    url="https://github.com/youtype/mypy_boto3_builder",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description=(
        "Type annotations for boto3.NimbleStudio 1.24.30 service generated with mypy-boto3-builder"
        " 7.9.0"
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    keywords="boto3 nimble type-annotations boto3-stubs mypy typeshed autocomplete",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"mypy_boto3_nimble": ["py.typed", "*.pyi"]},
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/",
        "Source": "https://github.com/youtype/mypy_boto3_builder",
        "Tracker": "https://github.com/youtype/mypy_boto3_builder/issues",
    },
    install_requires=[
        "typing-extensions>=4.1.0",
    ],
    zip_safe=False,
)
