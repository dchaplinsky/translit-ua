from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='translitua',

    version='1.0.0b1',

    description='Transliteration for ukrainian language',
    long_description=long_description,

    url='https://github.com/dchaplinsky/translit-ua',

    author='dchaplinsky',
    author_email='dchaplinsky@example.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='ukrainian transliteration',

    packages=[
        'translitua',
    ],

    package_data={'': ['LICENSE']},
)
