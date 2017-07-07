#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""FlaskApp Module."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from .config import config_by_name

db = SQLAlchemy()
toolbar = DebugToolbarExtension()


def create_app(config_name):
    """Create Flask App."""
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    toolbar.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')
    return app
