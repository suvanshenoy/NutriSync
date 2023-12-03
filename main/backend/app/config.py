import os


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'mysql://user:string name@localhost/userdb')
SQLALCHEMY_TRACK_MODIFICATIONS = False



