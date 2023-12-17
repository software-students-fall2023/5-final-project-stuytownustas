import pytest
from app import app
from bson import ObjectId
from unittest.mock import MagicMock

# Setup a fixture for the test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test the index route
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the StuyTown Task Manager!" in response.data

# Test adding a new task
def test_add_task(client):
    response = client.post('/tasks', data={'description': 'New Task'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'New Task' in response.data

# Test searching for a task
def test_search_task(client):
    # Mocking the database call for the purpose of this example
    with pytest.MonkeyPatch.context() as m:
        m.setattr('pymongo.collection.Collection.find', MagicMock(return_value=[{'_id': ObjectId(), 'description': 'Test Task'}]))
        response = client.get('/tasks?search=Test')
        assert response.status_code == 200
        assert b'Test Task' in response.data


# pytest test_app.py
# pytest --cov=app --cov-report=term-missing

# Test deleting a task
def test_delete_task(client):
    # Assuming we have a task with a specific ID
    test_id = ObjectId()
    response = client.post(f'/tasks/delete/{test_id}', follow_redirects=True)
    assert response.status_code == 200
