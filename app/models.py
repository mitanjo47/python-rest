# models.py
# pylint: disable=missing-docstring

from wsgi import db

class Product(db.Model):
    __tablename__ = "t_product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)