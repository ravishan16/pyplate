from datetime import datetime

from sqlalchemy import desc
from flaskapp import db

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")

class User(db.Model):
    __tablename__ = 'user_t'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    createddate = db.Column(db.DateTime, default=datetime.utcnow)
    modifieddate = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'   : self.id,
           'email' : self.email,
           'first_name' : self.first_name,
           'last_name': self.last_name,
           'createddate': dump_datetime(self.createddate),
           'modifieddate': dump_datetime(self.modifieddate)
       }

    def __repr__(self):
        return "<User '{}'>".format(self.first_name)