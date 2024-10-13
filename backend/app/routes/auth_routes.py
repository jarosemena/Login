from flask import Blueprint
from app.controllerscontrollers.auth_controller import auth_controller

auth_bp = Blueprint('auth', __name__)

auth_bp.add_url_rule('/auth', view_func=auth_controller.get_users, methods=['GET'])