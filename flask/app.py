from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration
items = {}

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items.values())), 200

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    item_id = data['id']
    if item_id in items:
        return jsonify({'error': 'Item already exists'}), 409
    items[item_id] = data
    return jsonify(data), 201

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    items[item_id]['name'] = data['name']
    return jsonify(items[item_id]), 200

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404
    del items[item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)