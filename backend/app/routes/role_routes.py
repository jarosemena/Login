from flask import Blueprint
from app.controllerscontrollers.role_controller import role_controller

role_bp = Blueprint('role', __name__)
role_bp.add_url_rule('/role', view_func=role_controller.get_roles, methods=['GET'])
role_bp.add_url_rule('/role', view_func=role_controller.create_role, methods=['POST'])
role_bp.add_url_rule('/role/<int:id>', view_func=role_controller.get_role, methods=['GET'])
role_bp.add_url_rule('/role/<int:id>', view_func=role_controller.update_role, methods=['PUT'])
role_bp.add_url_rule('/role/<int:id>', view_func=role_controller.delete_role, methods=['DELETE'])