from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'message': 'Error registering user', 'error': str(e)}), 500

@user_controller.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login failed! Check email and password'}), 401
    
    return jsonify({'message': 'Login successful!'}), 200

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []
    
    for user in users:
        user_data = {'id': user.id, 'username': user.username, 'email': user.email}
        result.append(user_data)
    
    return jsonify({'users': result}), 200