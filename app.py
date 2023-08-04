from flask import Flask, jsonify, request
import json

app = Flask(__name__)


def remove_duplicates():
    with open('fruits.json') as file:
        fruits = json.load(file)

    unique_fruits = []
    seen_ids = set()

    for fruit in fruits['fruits']:
        if fruit['id'] not in seen_ids:
            unique_fruits.append(fruit)
            seen_ids.add(fruit['id'])

    fruits['fruits'] = unique_fruits

    with open('fruits.json', 'w') as file:
        json.dump(fruits, file)


@app.route('/api/fruits', methods=['GET'])
def get_fruits():
    with open('fruits.json') as file:
        fruits = json.load(file)
    return jsonify(fruits['fruits'])


@app.route('/api/fruits/<int:id>', methods=['GET'])
def get_fruit(fruit_id: int):
    with open('fruits.json') as file:
        fruits = json.load(file)
    for fruit in fruits['fruits']:
        if fruit['id'] == fruit_id:
            return jsonify(fruit)
    return jsonify({'message': 'Fruit not found.'}), 404


@app.route('/api/fruits', methods=['POST'])
def create_fruit():
    new_fruit = request.get_json()
    with open('fruits.json') as file:
        fruits = json.load(file)

    for fruit in fruits['fruits']:
        if fruit['name'] == new_fruit['name']:
            return jsonify({'message': 'Fruit already exists. Use PUT to update the existing fruit.'}), 400

    fruits['fruits'].append(new_fruit)

    with open('fruits.json', 'w') as file:
        json.dump(fruits, file)

    return jsonify({'message': 'Fruit created successfully.'}), 201


@app.route('/api/fruits/<int:id>', methods=['PUT'])
def update_fruit(fruit_id: int):
    updated_fruit = request.get_json()
    with open('fruits.json') as file:
        fruits = json.load(file)
    for fruit in fruits['fruits']:
        if fruit['id'] == fruit_id:
            fruit.update(updated_fruit)
            with open('fruits.json', 'w') as file:
                json.dump(fruits, file)
            return jsonify({'message': 'Fruit updated successfully.'}), 200
    return jsonify({'message': 'Fruit not found.'}), 404


@app.route('/api/fruits/<int:id>', methods=['DELETE'])
def delete_fruit(fruit_id: int):
    with open('fruits.json') as file:
        fruits = json.load(file)
    for fruit in fruits['fruits']:
        if fruit['id'] == fruit_id:
            fruits['fruits'].remove(fruit)
            with open('fruits.json', 'w') as file:
                json.dump(fruits, file)
            return jsonify({'message': 'Fruit deleted successfully.'}), 200
    return jsonify({'message': 'Fruit not found.'}), 404


@app.route('/api/fruits/search', methods=['GET'])
def search_fruit():
    name = request.args.get('name')
    with open('fruits.json') as file:
        fruits = json.load(file)
    matching_fruits = [fruit for fruit in fruits['fruits'] if fruit['name'].lower() == name.lower()]
    return jsonify(matching_fruits)


if __name__ == '__main__':
    app.run(debug=True)
