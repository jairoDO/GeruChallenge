from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='quote_lib',
    version='0.1.1',
    description='Wrap lib of the api rest https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes',
    long_description=long_description,
    url='https://pypi.python.org/pypi/pysaurio',
    author='Jairo ordonez',
    author_email='jairo222@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    install_requires=['requests'],
    keywords='lib challenge tencique-test',
    packages=['quote_lib'],
    package_dir = {'quote_lib':'quote_lib'},
)