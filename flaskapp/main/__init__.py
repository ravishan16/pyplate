#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""FlaskApp Main Module."""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import api