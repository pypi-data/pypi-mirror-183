from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'readme.md'), encoding = 'utf-8') as fh:
        LONG_DESCRIPTION = fh.read()


VERSION = '0.0.1'
DESCRIPTION = 'Library Time'

setup(
name = 'Library Time',
version = VERSION,
auther = 'Maryam Modaresi',
auther_email = 'modaresianita05@gmail.com',
description = DESCRIPTION,
long_description_content_type = 'text/markdown',
long_description = LONG_DESCRIPTION,
packages = find_packages(),
install_requires = [],
keywords = ['Time','python'],
classifiers = [
'Development Status :: 1 - Planning',
'Intended Audience :: Developers',
'Programming Language :: Python :: 3',
'Operating System :: Unix',
'Operating System :: MacOS :: MacOS X',
'Operating System :: Microsoft :: Windows',
]
)
