from flask import Blueprint
from app.controllers.user_controller import user_controller

user_bp = Blueprint('user', __name__)
user_bp.add_url_rule('/users', view_func=user_controller.get_users, methods=['GET'])
user_bp.add_url_rule('/users', view_func=user_controller.create_user, methods=['POST'])
user_bp.add_url_rule('/users/<int:id>', view_func=user_controller.get_user, methods=['GET'])
user_bp.add_url_rule('/users/<int:id>', view_func=user_controller.update_user, methods=['PUT'])

