from setuptools import setup

with open("README.md", "r") as f:

    long_description = f.read()

setup(
    requires = ["setuptools", "wheel"],
    name="hexacolors",
    version="0.6.0b1",
    url = 'https://github.com/Marciel404/hexacolors',
    author="Marciel404",
    description='''
:A simple library that converts string to hexadecimal understandable by python
:A simple library that converts RGB to hexadecimal understandable by python
:A simple library that converts CMYK to hexadecimal understandable by python
:A simple library that converts HSL to hexadecimal understandable by python
:A simple library that converts hexadecimal understandable by python
''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["hexacolors", "hexacolors.colors", "hexacolors.offline", "hexacolors.online"],
    license = 'MIT',
    keywords = 'String hexadecimal converter' ,
    classifiers = [
    'Intended Audience :: Developers',
    'Topic :: Utilities',
    'Programming Language :: Python',
    ],
    python_requires='>=3.10',
    dependency_links=['https://github.com/Marciel404/hexacolors']
)