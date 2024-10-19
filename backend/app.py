from flask import Flask
from extensions import db
from flask_migrate import Migrate
from config import Config

from app import create_app

app = create_app(Config)

migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)