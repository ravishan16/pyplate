#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""FlaskApp Main Module."""

from flask import jsonify
from flask import make_response
from flask import request
from flask import abort
from sqlalchemy import exc
from .. import db
from . import main
from .models import User

@main.route('/users', methods=['GET', 'POST'])
def getUsers():
    """Get All User."""
    user = User.query.all()
    return make_response(jsonify(users=[i.serialize for i in user]), 200)


@main.route('/user/<email>', methods=['GET', 'POST'])
def getUser(email):
    """Get User by Email."""
    user = User.query.filter_by(email=email).first_or_404()
    return make_response(jsonify(user.serialize), 200)


@main.route('/add/user', methods=['POST'])
def addUser():
    """Add User."""
    data = request.json
    try:
        user = User(data['email'], data['first_name'], data['last_name'])
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError as e:
        db.session().rollback()
        abort(409)
    except:
        abort(500)
    return make_response(jsonify(user.serialize), 200)


@main.errorhandler(404)
def not_found(error):
    """404 Error."""
    return make_response(jsonify({'error': 'Data Not found'}), 404)


@main.errorhandler(400)
def not_found(error):
    """400 Error."""
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@main.errorhandler(409)
def not_found(error):
    """404 Error."""
    return make_response(jsonify({'error': 'Data Integrity Error'}), 409)


@main.app_errorhandler(500)
def internal_server_error(e):
    """Server Error."""
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)
