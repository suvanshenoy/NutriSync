

from app import db
from datetime import datetime


'''DATABASE CLASS FOR SIGN-UP PAGE'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # name = db.Column(db.String(80),unique=True,nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer,nullable=False)
    dob = db.Column(db.Date,nullable=False)
    gender = db.Column(db.String(10),nullable=False)
    signup_date = db.Column(db.DateTime,default=datetime.utcnow)


    def __init__(self,first_name,last_name,email,password,age,dob,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.age = age
        self.dob = dob
        self.gender = gender


