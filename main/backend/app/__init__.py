# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    CORS(app,methods=["GET","POST"])

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app
