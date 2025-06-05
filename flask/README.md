# Flask REST API Example

This is a basic Flask project demonstrating REST API endpoints for GET, POST, PUT, and DELETE using in-memory storage.

## Endpoints
- `GET /items` - List all items
- `POST /items` - Create a new item (expects JSON: `{ "id": "unique_id", "name": "Item Name" }`)
- `PUT /items/<item_id>` - Update an existing item's name (expects JSON: `{ "name": "New Name" }`)
- `DELETE /items/<item_id>` - Delete an item

## Running the Project
1. Install dependencies:
   ```bash
   pipenv install
   ```
2. Start the server:
   ```bash
   python app.py
   ```

## Notes
- Data is stored in memory and will be lost when the server restarts.

## Example curl Commands for Testing Endpoints

### 1. List all items (GET)
```bash
curl http://localhost:5000/items
```

### 2. Create a new item (POST)
```bash
curl -X POST http://localhost:5000/items \
  -H "Content-Type: application/json" \
  -d '{"id": "1", "name": "Item 1"}'
```

### 3. Update an existing item's name (PUT)
```bash
curl -X PUT http://localhost:5000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item 1"}'
```

### 4. Delete an item (DELETE)
```bash
curl -X DELETE http://localhost:5000/items/1
```

## Test

### 1. Run all tests
```bash
pytest
```
Ensure the tests are named test_*.py or *_test.py.

### 2. Run test in folder
```bash
PYTHONPATH=/home/carlos/Documents/rest_api/flask pytest tests/
```

### 3. Run specific file
```bash
PYTHONPATH=/home/carlos/Documents/rest_api/flask pytest
```

### 4. Run specific test
```bash
PYTHONPATH=/home/carlos/Documents/rest_api/flask pytest test_app.py -k test_create_item_success
```