import pytest


def test_get_boards(test_client):
    response = test_client.get('api/v1/boards')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert 'boards' in response.json


def test_create_board(test_client):
    response = test_client.post('api/v1/boards')
    assert response.status_code == 201
    assert isinstance(response.json, dict)
    assert 'board' in response.json


def test_get_board(test_client):
    create_response = test_client.post('api/v1/boards')
    board_id = create_response.json['board']['id']

    response = test_client.get(f'api/v1/boards/{board_id}')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert 'board' in response.json
    assert response.json['board']['id'] == board_id


def test_update_board_status(test_client):
    create_response = test_client.post('api/v1/boards')
    board_id = create_response.json['board']['id']

    update_data = {'status': 'archived'}
    response = test_client.put(f'api/v1/boards/{board_id}/status', json=update_data)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert 'message' in response.json
