#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for flaskapp."""

from flaskapp import create_app, db
import json
from flask_testing import TestCase
from flaskapp.main.models import User


class TestFlaskApp(TestCase):
    """TestFlaskApp class."""

    def create_app(self):
        """Create Flask App."""
        return create_app('test')

    def setUp(self):
        """Setup Flask db."""
        db.create_all()
        self.client = self.app.test_client()
        self.app.testing = True
        user = User('a.a@a.com', 'a', 'a')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """Test Suite Tear down."""
        db.session.remove()
        db.drop_all()

    def test_getusers(self):
        """Test get all users ."""
        result = self.client.get('/main/users')
        print result.json
        assert result.status_code == 200

    def test_addusers(self):
        """Test add users ."""
        payload = json.dumps(dict(
            email="a.b@a.com",
            first_name="a",
            last_name="b"
        ))
        result = self.client.post('main/add/user',
                                  data=payload,
                                  content_type='application/json')
        print result
        assert result.status_code == 200

    def test_dupusers(self):
        """Test duplicate users ."""
        payload = json.dumps(dict(
            email="a.a@a.com",
            first_name="a",
            last_name="b"
        ))
        # print json.dumps(data)
        result = self.client.post('main/add/user',
                                  data=payload,
                                  content_type='application/json')
        print result
        assert result.status_code == 409

    def test_getuser(self):
        """Test get user ."""
        result = self.client.post('main/user/a.a@a.com')
        print result
        assert result.status_code == 200

    def test_getnouser(self):
        """Test get no user ."""
        result = self.client.post('main/user/c.a@a.com')
        print result
        assert result.status_code == 404

    def test_servererror(self):
        """Test get no user ."""
        payload = json.dumps(dict(
            email="c@a.com",
            first_name=None,
            last_name=None
        ))
        # print json.dumps(data)
        result = self.client.post('main/add/user',
                                  data=payload,
                                  content_type='application/json')
        print result
        assert result.status_code == 409
