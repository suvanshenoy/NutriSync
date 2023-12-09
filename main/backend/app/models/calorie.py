from app import db

class Calorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self,amount):
        pass
