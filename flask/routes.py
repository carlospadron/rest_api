from flask import Blueprint, request, current_app

bp = Blueprint('main', __name__)

@bp.route('/')
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

@bp.route('/items', methods=['GET'])
def get_items():
    return list(current_app.items.values()), 200

@bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return {'error': 'Invalid input'}, 400
    item_id = data['id']
    if item_id in current_app.items:
        return {'error': 'Item already exists'}, 409
    current_app.items[item_id] = data
    return data, 201

@bp.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in current_app.items:
        return {'error': 'Item not found'}, 404
    data = request.get_json()
    if not data or 'name' not in data:
        return {'error': 'Invalid input'}, 400
    current_app.items[item_id]['name'] = data['name']
    return current_app.items[item_id], 200

@bp.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in current_app.items:
        return {'error': 'Item not found'}, 404
    del current_app.items[item_id]
    return '', 204

def init_app(app):
    app.register_blueprint(bp)