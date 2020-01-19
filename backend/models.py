from flask_sqlalchemy import SQLAlchemy
from app import db

class TestRow(db.Model):
    __tablename__ = 'test_rows'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String())

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<id {self.id}> <data {self.data}>"


class TestRow2(db.Model):
    __tablename__ = 'test_rows2'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String())

    def __repr__(self):
        return f"<id {self.id}> <data {self.data}>"