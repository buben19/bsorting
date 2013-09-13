from __future__ import unicode_literals
from setuptools import setup, find_packages
import os



def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

required = ['zope.interface']
setup(
    name                        = 'bsorting',
    version                     = '0.0.1',
    author                      = 'Ivo Slanina',
    author_email                = 'ivo.slanina@gmail.com',
    description                 = 'Library with sorting algorithms',
    licence                     = 'Unlicence',
    keywords                    = 'sort, sorting algorithms',
    url                         = 'https://github.com/buben19/bsorting',
    long_description            = read('README.md'),
    classifiers                 = [],
    install_requires            = required,
    packages                    = find_packages())
