from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.rolesuser import RolesUser
from extensions import db

class rolesuser_controller:
    def get_role_by_user_id(user_id):
        role = RolesUser.query.filter_by(user_id=user_id).first_or_404()
        return jsonify(role.to_dict())

    def create_role_for_user(user_id):
        data = request.get_json()
        new_role = RolesUser(user_id=user_id, role_name=data['role_name'])
        db.session.add(new_role)
        db.session.commit()
        return jsonify(new_role.to_dict()), 201

    def delete_all_roles_by_user_id(user_id):
        roles = RolesUser.query.filter_by(user_id=user_id).all()
        for role in roles:
            db.session.delete(role)
        db.session.commit()
        return '', 204
        
    def delete_role_by_user_and_role_id(user_id, role_id):
        role = RolesUser.query.filter_by(user_id=user_id, role_id=role_id).first_or_404()
        db.session.delete(role)
        db.session.commit()
        return '', 204



