from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store users
users = {}

@app.route('/users', methods=['POST'])
def create_user():
    # Parse incoming JSON request
    user_data = request.json
    
    # Assign a simple unique ID (length of dict + 1)
    user_id = str(len(users) + 1)
    user_data['id'] = user_id
    
    # Store in our dictionary
    users[user_id] = user_data
    
    # Return 201 Created and the new data
    return jsonify(user_data), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # Look up user in dictionary
    user = users.get(user_id)
    
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)