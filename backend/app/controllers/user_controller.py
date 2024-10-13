from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from extensions import db

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user_data = {'id': user.id, 'username': user.username, 'email': user.email}
    return jsonify({'user': user_data}), 200

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []
    
    for user in users:
        user_data = {'id': user.id, 'username': user.username, 'email': user.email}
        result.append(user_data)
    
    return jsonify({'users': result}), 200