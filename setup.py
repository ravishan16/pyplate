#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""setup for flaskapp."""

from setuptools import setup

setup(
    name='flaskapp',
    version='0.0.1',
    url='https://github.com/ravishan16/flaskapp',
    license='MIT',
    author='Ravishankar Sivasubramaniam',
    author_email='ravi_siva@live.com',
    description='REST API using Python Flask/SQLAlchemy/SQLite',
    packages=['flaskapp'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.12',
        'SQLAlchemy>=1.1.6',
        'Flask-SQLAlchemy>=2.2',
        'pylint',
        'nose',
        'flask_debugtoolbar',
        'Flask-Script',
        'Flask-Migrate',
        'flask_testing',
        'coverage>=4.0,<4.4'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
