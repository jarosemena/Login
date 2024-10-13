from flask import Blueprint
from app.controllers.roles_controller import roles_controller

user_bp = Blueprint('user', __name__)
user_bp.add_url_rule('/users', view_func=roles_controller.get, methods=['GET'])
user_bp.add_url_rule('/users', view_func=roles_controller.create_user, methods=['POST'])
user_bp.add_url_rule('/users/<int:id>', view_func=roles_controller.get_user, methods=['GET'])
user_bp.add_url_rule('/users/<int:id>', view_func=roles_controller.update_user, methods=['PUT'])

