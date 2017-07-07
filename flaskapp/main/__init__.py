#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""FlaskApp Main Module."""
from . import api
from flask import Blueprint

main = Blueprint('main', __name__)
