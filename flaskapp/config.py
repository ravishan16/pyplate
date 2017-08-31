#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration File for flaskapp."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Config Class."""

    # os.urandom(24)
    SECRET_KEY = '\xa4?\xca`\xa4~zG\xdf\xdbh\xba\xc2\xc6\xfc\x88\xc6x"\x11\xe8X8\n'
    DEBUG = False


class DevelopmentConfig(Config):
    """Config Class DevelopmentConfig."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db',
                                                          'flaskapp-dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Config Class TestingConfig."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db',
                                                          'flaskapp-test.db')
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "localhost"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Config Class ProductionConfig."""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db',
                                                          'flaskapp-prod.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
config_by_name = dict(
                        dev=DevelopmentConfig,
                        test=TestingConfig,
                        prod=ProductionConfig
                    )
