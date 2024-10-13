from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from app import create_app

app = create_app()

app = Flask(__name__)
app.config.from_object(Config)

from app.routes.user_routes import user_bp
from app.routes.auth_routes import auth_bp
from app.routes.role_routes import role_bp
from app.routes.rolesuser_routes import rolesuser_bp

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(role_bp, url_prefix='/api')
app.register_blueprint(rolesuser_bp, url_prefix='/api')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)