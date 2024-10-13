from flask_sqlalchemy import SQLAlchemy
from extensions import db

class RolesUser(db.Model):
    __tablename__ = 'roles_user'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('roles_user', lazy=True))
    role = db.relationship('Role', backref=db.backref('roles_user', lazy=True))

    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id

    def __repr__(self):
        return f'<RolesUser {self.user_id} - {self.role_id}>'