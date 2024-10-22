# tests/test_user_controller.py
import pytest
from app import create_app
from extensions import db
from app.models.user import User
from app.tests.test_config import TestConfig

@pytest.fixture
def app():
    app = create_app(config_class=TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_user_by_id(client):
    user = User(username='testuser', email='testuser@example.com', password_hash='hashedpassword')
    db.session.add(user)
    db.session.commit()
    response = client.get(f'/user/{user.id}')
    assert response.status_code == 200
    assert response.get_json()['user']['username'] == 'testuser'

def test_get_users(client):
    user1 = User(username='testuser1', email='testuser1@example.com', password_hash='hashedpassword1')
    user2 = User(username='testuser2', email='testuser2@example.com', password_hash='hashedpassword2')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    response = client.get('/users')
    assert response.status_code == 200
    users = response.get_json()['users']
    assert len(users) == 2
    assert users[0]['username'] == 'testuser1'
    assert users[1]['username'] == 'testuser2'