from .import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_migrate import Migrate


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    product = db.relationship('Product')



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150))
    description = db.Column(db.String(10000))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer_firstname = db.Column(db.String(150))
    employer_lastname = db.Column(db.String(150))
    description = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
