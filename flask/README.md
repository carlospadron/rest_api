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
