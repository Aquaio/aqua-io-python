import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='aqua-io',
    version='0.1.0',
    description='Official Aqua.io API library client for Python',
    author='Michael Carroll / Aqua.io',
    author_email='michael@aqua.io',
    url='https://aqua.io',
    download_url='https://github.com/Aquaio/aqua-io-python/tarball/0.1',
    keywords=[
        'aqua',
        'aqua.io',
        'api',
        'client',
        'library',
        'ICD',
        'ICD9',
        'ICD10',
        'ICD-9',
        'ICD-10',
        'meaningful use',
        'healthcare',
        'health',
        'EHR',
        'EMR',
        'medicine',
        'medical'
    ],
    license='MIT',
    install_requires=[
        'requests >= 2.1.0'
    ],
    packages=[
        'aqua_io',
        'aqua_io.api',
        'aqua_io.error',
        'aqua_io.http_client'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
