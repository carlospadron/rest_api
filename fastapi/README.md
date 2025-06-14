# FastAPI REST API Example

This is a basic FastAPI project demonstrating REST API endpoints for GET, POST, PUT, and DELETE using in-memory storage.

## Installation

1. Install dependencies using pipenv:
   ```bash
   pipenv install "fastapi[standard]"
   ```

2. (Optional) If you don't have `pipenv`, install it with:
   ```bash
   pip install pipenv
   ```

## Running the Project

Start the development server with:
```bash
pipenv run fastapi dev main.py
```
Or, using uvicorn directly:
```bash
pipenv run uvicorn main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000)

## Endpoints
- `GET /items` - List all items
- `POST /items` - Create a new item (expects JSON: `{ "id": "unique_id", "name": "Item Name" }`)
- `PUT /items/{item_id}` - Update an existing item's name (expects JSON: `{ "name": "New Name" }`)
- `DELETE /items/{item_id}` - Delete an item

## Example curl Commands for Testing Endpoints

### 1. List all items (GET)
```bash
curl http://localhost:8000/items
```

### 2. Create a new item (POST)
```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"id": "1", "name": "Item 1"}'
```

### 3. Update an existing item's name (PUT)
```bash
curl -X PUT http://localhost:8000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item 1"}'
```

### 4. Delete an item (DELETE)
```bash
curl -X DELETE http://localhost:8000/items/1
```

## Interactive API Docs

Once the server is running, you can access the interactive documentation at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Notes
- Data is stored in memory and will be lost when the server restarts.
- For production, use a WSGI server like Uvicorn or Gunicorn.