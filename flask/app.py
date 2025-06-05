from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration
items = {}

@app.route('/')
def index():
    return (
        "<h1>Welcome to the Item Management API!</h1>"
        "<h2>Available endpoints:</h2>"
        "<ul>"
        "<li><b>GET</b> /items - List all items</li>"
        "<li><b>POST</b> /items - Create a new item<br>"
        "&nbsp;&nbsp;Body: <code>{\"id\": str, \"name\": str}</code></li>"
        "<li><b>PUT</b> /items/&lt;item_id&gt; - Update an item name<br>"
        "&nbsp;&nbsp;Body: <code>{\"name\": str}</code></li>"
        "<li><b>DELETE</b> /items/&lt;item_id&gt; - Delete an item</li>"
        "</ul>"
    )

@app.route('/items', methods=['GET'])
def get_items():
    return list(items.values()), 200

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return {'error': 'Invalid input'}, 400
    item_id = data['id']
    if item_id in items:
        return {'error': 'Item already exists'}, 409
    items[item_id] = data
    return data, 201

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in items:
        return {'error': 'Item not found'}, 404
    data = request.get_json()
    if not data or 'name' not in data:
        return {'error': 'Invalid input'}, 400
    items[item_id]['name'] = data['name']
    return items[item_id], 200

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return {'error': 'Item not found'}, 404
    del items[item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)