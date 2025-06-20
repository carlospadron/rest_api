import pytest
from fastapi.testclient import TestClient
from main import app, items

@pytest.fixture(autouse=True)
def clear_items():
    items.clear()

@pytest.fixture
def client():
    return TestClient(app)

def test_get_items_empty(client):
    resp = client.get('/items')
    assert resp.status_code == 200
    assert resp.json() == []

def test_create_item_success(client):
    resp = client.post('/items', json={'id': '1', 'name': 'Item 1'})
    assert resp.status_code == 201
    assert resp.json() == {'id': '1', 'name': 'Item 1'}

def test_create_item_missing_fields(client):
    resp = client.post('/items', json={'id': '2'})
    assert resp.status_code == 422  # FastAPI returns 422 for validation errors

def test_create_item_duplicate(client):
    client.post('/items', json={'id': '1', 'name': 'Item 1'})
    resp = client.post('/items', json={'id': '1', 'name': 'Item 1'})
    assert resp.status_code == 409
    assert resp.json()['detail'] == 'Item already exists'

def test_get_items_nonempty(client):
    client.post('/items', json={'id': '1', 'name': 'Item 1'})
    resp = client.get('/items')
    assert resp.status_code == 200
    assert resp.json() == [{'id': '1', 'name': 'Item 1'}]

def test_update_item_success(client):
    client.post('/items', json={'id': '1', 'name': 'Item 1'})
    resp = client.put('/items/1', json={'name': 'Updated'})
    assert resp.status_code == 200
    assert resp.json() == {'id': '1', 'name': 'Updated'}

def test_update_item_not_found(client):
    resp = client.put('/items/999', json={'name': 'Updated'})
    assert resp.status_code == 404
    assert resp.json()['detail'] == 'Item not found'

def test_update_item_invalid_input(client):
    client.post('/items', json={'id': '1', 'name': 'Item 1'})
    resp = client.put('/items/1', json={})
    assert resp.status_code == 422  # FastAPI returns 422 for validation errors

def test_delete_item_success(client):
    client.post('/items', json={'id': '1', 'name': 'Item 1'})
    resp = client.delete('/items/1')
    assert resp.status_code == 204

def test_delete_item_not_found(client):
    resp = client.delete('/items/999')
    assert resp.status_code == 404
    assert resp.json()['detail'] == 'Item not found'
