from users import *


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'Users': User.get_all_users()})

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return_value = User.get_user(id)
    return jsonify(return_value)

@app.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()
    User.add_user(request_data["name"], request_data["age"],
                    request_data["sexe"])
    response = Response("User added", 201, mimetype='application/json')
    return response

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    request_data = request.get_json()
    User.update_user(id, request_data['name'], request_data['age'], request_data['sexe'])
    response = Response("User Updated", status=200, mimetype='application/json')
    return response

@app.route('/users/<int:id>', methods=['DELETE'])
def remove_user(id):
    User.delete_user(id)
    response = Response("User Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)