from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {}

# Get all users or a specific user
@app.route('/users', methods=['GET'])
def get_users():
    user_id = request.args.get('id')
    if user_id:
        user = users.get(user_id)
        if user:
            return jsonify({user_id: user}), 200
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users), 200

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = str(data.get('id'))
    if not user_id or user_id in users:
        return jsonify({'error': 'Invalid or existing user ID'}), 400
    users[user_id] = {'name': data.get('name'), 'age': data.get('age')}
    return jsonify({'message': 'User added'}), 201

# Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.json
    users[user_id].update({'name': data.get('name'), 'age': data.get('age')})
    return jsonify({'message': 'User updated'}), 200

# Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[user_id]
    return jsonify({'message': 'User deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
