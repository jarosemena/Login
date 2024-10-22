from flask import Flask
from extensions import db
from flask_migrate import Migrate
from config import Config
import logging

from app import create_app

app = create_app(Config)

with app.app_context():
    db.create_all()        
    migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
