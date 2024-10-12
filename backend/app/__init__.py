from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configuración de la aplicación
    app.config.from_object('config.Config')

    # Registro de blueprints
    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    return app