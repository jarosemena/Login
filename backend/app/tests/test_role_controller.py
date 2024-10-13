# tests/test_role_controller.py
import pytest
from app import create_app 
from extensions import db
from app.models.role import Role
from app.tests.test_config import TestConfig

@pytest.fixture
def app():
    app = create_app(config_class=TestConfig)
    with app.app_context():
        db.init_app(app)
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_role(client):
    response = client.post('/role', json={'name': 'Admin'})
    assert response.status_code == 201
    assert response.get_json()['name'] == 'Admin'

def test_update_role(client):
    role = Role(name='User')
    db.session.add(role)
    db.session.commit()
    response = client.put(f'/role/{role.id}', json={'name': 'SuperUser'})
    assert response.status_code == 200
    assert response.get_json()['name'] == 'SuperUser'

def test_delete_role(client):
    role = Role(name='Guest')
    db.session.add(role)
    db.session.commit()
    response = client.delete(f'/role/{role.id}')
    assert response.status_code == 204