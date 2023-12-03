from app import db


'''
DATABASE CLASS FOR SIGN-IN PAGE
'''
class SignIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255),nullable=False)
    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password


    

