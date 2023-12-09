from app import db

class Meal(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    calories = db.Column(db.Integer,nullable=False)

    def __init__(self,name,calories):
        pass

