from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config.from_object(Config)

    # Registro de blueprints
    from app.routes.user_routes import user_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.role_routes import role_bp
    from app.routes.rolesuser_routes import rolesuser_bp

    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(role_bp, url_prefix='/api')
    app.register_blueprint(rolesuser_bp, url_prefix='/api')

    return app