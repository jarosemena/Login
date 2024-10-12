from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from app import create_app

app = create_app()

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:contraseña@localhost/mi_proyecto'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)

# Importa y registra tus rutas aquí
from app.routes.user_routes import user_bp
from app.routes.auth_routes import auth_bp

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)