from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='saganvm',
    version='1.2.3',
    packages=['sagan'],
    url='',
    license='',
    author='T A H Smith, A W Collins, Jeff Trotman',
    author_email='jtrotman@dreamup.org',
    description='Python library for simulating experiment results',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
