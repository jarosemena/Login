from flask import Blueprint, request, jsonify
from app.models.role import Role
from extensions import db

class role_controller:

    def get_roles():
        roles = Role.query.all()
        return jsonify([role.to_dict() for role in roles])

    def get_role(id):
        role = Role.query.get_or_404(id)
        return jsonify(role.to_dict())

    def create_role():
        data = request.get_json()
        new_role = Role(name=data['name'])
        db.session.add(new_role)
        db.session.commit()
        return jsonify(new_role.to_dict()), 201

    def update_role(id):
        role = Role.query.get_or_404(id)
        data = request.get_json()
        role.name = data['name']
        db.session.commit()
        return jsonify(role.to_dict())

    def delete_role(id):
        role = Role.query.get_or_404(id)
        db.session.delete(role)
        db.session.commit()
        return '', 204