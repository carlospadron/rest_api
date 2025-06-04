import unittest
from flask import json

# python

from flask.app import app, items  # Absolute import from namespace package

class ItemApiTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        items.clear()

    def test_get_items_empty(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_create_item_success(self):
        data = {'id': '1', 'name': 'Item1'}
        response = self.client.post('/items', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), data)

    def test_create_item_missing_fields(self):
        response = self.client.post('/items', json={'id': '2'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_create_item_duplicate(self):
        data = {'id': '1', 'name': 'Item1'}
        self.client.post('/items', json=data)
        response = self.client.post('/items', json=data)
        self.assertEqual(response.status_code, 409)
        self.assertIn('error', response.get_json())

    def test_get_items_non_empty(self):
        data = {'id': '1', 'name': 'Item1'}
        self.client.post('/items', json=data)
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [data])

    def test_update_item_success(self):
        data = {'id': '1', 'name': 'Item1'}
        self.client.post('/items', json=data)
        response = self.client.put('/items/1', json={'name': 'Updated'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Updated')

    def test_update_item_not_found(self):
        response = self.client.put('/items/999', json={'name': 'Nope'})
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

    def test_update_item_invalid_input(self):
        data = {'id': '1', 'name': 'Item1'}
        self.client.post('/items', json=data)
        response = self.client.put('/items/1', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_delete_item_success(self):
        data = {'id': '1', 'name': 'Item1'}
        self.client.post('/items', json=data)
        response = self.client.delete('/items/1')
        self.assertEqual(response.status_code, 204)

    def test_delete_item_not_found(self):
        response = self.client.delete('/items/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()