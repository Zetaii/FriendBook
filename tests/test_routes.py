import pytest
from app import create_app, db
import json

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/friendbook_test'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to FriendBook API!" in response.data

def test_create_user(client):
    data = {
        "username": "testuser",
        "email": "test@example.com"
    }
    response = client.post('/users',
                          data=json.dumps(data),
                          content_type='application/json')
    
    assert response.status_code == 201
    assert "User created successfully" in response.get_json()["message"] 