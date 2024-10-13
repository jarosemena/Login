from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from extensions import db
from flask import session
from app.models.token_blacklist import TokenBlacklist
import jwt
import datetime


class auth_controller:
    def register():
        data = request.get_json()
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'message': 'Invalid data'}), 400

        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(username=data['username'], password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'User registered successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'User registration failed', 'error': str(e)}), 500

    def login():
        data = request.get_json()
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'message': 'Invalid data'}), 400

        user = User.query.filter_by(username=data['username']).first()
        if not user or not check_password_hash(user.password, data['password']):
            return jsonify({'message': 'Invalid username or password'}), 401

        # Here you would generate a token and return it
        # Generate token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, 'your_secret_key', algorithm='HS256')

        # Store the token in the database (assuming you have a Token model)
        new_token = TokenBlacklist(user_id=user.id, token=token)
        try:
            db.session.add(new_token)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Token generation failed', 'error': str(e)}), 500
        token = 'your_generated_token_here'
        return jsonify({'message': 'Login successful', 'token': token}), 200

    def change_password():
        data = request.get_json()
        if not data or not data.get('username') or not data.get('old_password') or not data.get('new_password'):
            return jsonify({'message': 'Invalid data'}), 400

        user = User.query.filter_by(username=data['username']).first()
        if not user or not check_password_hash(user.password, data['old_password']):
            return jsonify({'message': 'Invalid username or password'}), 401

        user.password = generate_password_hash(data['new_password'], method='sha256')
        try:
            db.session.commit()
            return jsonify({'message': 'Password changed successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Password change failed', 'error': str(e)}), 500
        
    def logout():
        # Here you would handle the logout logic, such as invalidating the token
        session.pop('username', None)
        # Assuming you have a token blacklist model to store invalidated tokens

        # Get the token from the request headers
        token = request.headers.get('Authorization').split()[1]

        # Add the token to the blacklist
        blacklisted_token = TokenBlacklist(token=token)
        try:
            db.session.add(blacklisted_token)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Logout failed', 'error': str(e)}), 500
        return jsonify({'message': 'Logout successful'}), 200

    def set_session():
        data = request.get_json()
        if not data or not data.get('username'):
            return jsonify({'message': 'Invalid data'}), 400

        session['username'] = data['username']
        return jsonify({'message': 'Session set successfully'}), 200

    def get_session():
        username = session.get('username')
        if not username:
            return jsonify({'message': 'No session found'}), 404

        return jsonify({'message': 'Session found', 'username': username}), 200

    def clear_session():
        session.pop('username', None)
        return jsonify({'message': 'Session cleared successfully'}), 200