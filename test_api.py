import requests


def test_get_fruits():
    response = requests.get('http://localhost:5000/api/fruits')
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_fruit():
    response = requests.get('http://localhost:5000/api/fruits/1')
    assert response.status_code == 200
    assert response.json()['name'] == 'Green Apple'


def test_create_fruit():
    new_fruit = {
        'id': 4,
        'name': 'Mango',
        'color': 'Yellow and Green'
    }
    response = requests.post('http://localhost:5000/api/fruits', json=new_fruit)
    assert response.status_code == 201
    assert response.json()['message'] == 'Fruit created successfully.'


def test_update_fruit():
    updated_fruit = {
        'name': 'Green Apple',
        'color': 'Green'
    }
    response = requests.put('http://localhost:5000/api/fruits/2', json=updated_fruit) # Исправленный ID
    assert response.status_code == 200
    assert response.json()['message'] == 'Fruit updated successfully.'


def test_delete_fruit():
    response = requests.delete('http://localhost:5000/api/fruits/4')
    assert response.status_code == 200
    assert response.json()['message'] == 'Fruit deleted successfully.'


def test_search_fruit():
    response = requests.get('http://localhost:5000/api/fruits/search?name=Green Apple')
    assert response.status_code == 200
    assert response.json()[0]['id'] == 1
