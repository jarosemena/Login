from flask import Flask
from extensions import db
from flask_migrate import Migrate

from app import create_app

app = create_app()

db.init_app(app)
    
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)