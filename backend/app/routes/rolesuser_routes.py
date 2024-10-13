from flask import Blueprint
from app.controllers.roles_controller import rolesuser_controller

rolesuser_bp = Blueprint('rolesuser', __name__)
rolesuser_bp.add_url_rule('/rolesuser/user/<int:user_id>', view_func=rolesuser_controller.get_role_by_user_id, methods=['GET'])
rolesuser_bp.add_url_rule('/rolesuser/user/<int:user_id>', view_func=rolesuser_controller.create_role_for_user, methods=['POST'])
rolesuser_bp.add_url_rule('/rolesuser/user/<int:user_id>', view_func=rolesuser_controller.delete_all_roles_by_user_id, methods=['DELETE'])
rolesuser_bp.add_url_rule('/rolesuser/user/<int:user_id>/role/<int:role_id>', view_func=rolesuser_controller.delete_role_by_user_and_role_id, methods=['DELETE'])

