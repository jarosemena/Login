from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

class application(config_class=Config) :
    def __init__(self): 
        self.app = create_app(config_class)
        self.db = null

    def create_app( config_class=config_class):
        app = Flask(__name__)
        # Configuración de la aplicación
        app = create_app(Config)
        app.config.from_object(config_class)

        self.db = SQLAlchemy(app)
        self.db.create_all()        
        migrate = Migrate(app, self.db)

        # Registro de blueprints
        from app.routes.user_routes import user_bp
        #from app.routes.auth_routes import auth_bp
        from app.routes.role_routes import role_bp
        from app.routes.rolesuser_routes import rolesuser_bp

        app.register_blueprint(user_bp, url_prefix='/api')
        #app.register_blueprint(auth_bp, url_prefix='/api')
        app.register_blueprint(role_bp, url_prefix='/api')
        app.register_blueprint(rolesuser_bp, url_prefix='/api')

        return app