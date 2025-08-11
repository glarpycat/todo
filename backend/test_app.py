import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    """Test case for GET /tasks"""
    rv = client.get('/tasks')
    assert rv.status_code == 200
    assert len(json.loads(rv.data)) == 2

def test_add_task(client):
    """Test case for POST /tasks"""
    rv = client.post('/tasks', json={'title': 'Learn pytest'})
    assert rv.status_code == 201
    data = json.loads(rv.data)
    assert data['title'] == 'Learn pytest'
    assert not data['done']

    # Check if the task was actually added
    rv = client.get('/tasks')
    assert len(json.loads(rv.data)) == 3

def test_update_task(client):
    """Test case for PUT /tasks/<id>"""
    rv = client.put('/tasks/2', json={'done': True})
    assert rv.status_code == 200
    data = json.loads(rv.data)
    assert data['done']

def test_delete_task(client):
    """Test case for DELETE /tasks/<id>"""
    rv = client.delete('/tasks/1')
    assert rv.status_code == 204

    # Check if the task was actually deleted
    rv = client.get('/tasks')
    assert len(json.loads(rv.data)) == 2 # It was 3 before this test
