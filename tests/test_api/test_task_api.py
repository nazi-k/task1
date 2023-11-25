import pytest


def create_test_board(test_client):
    response = test_client.post('api/v1/boards')
    return response.json['board']['id']


def test_get_tasks(test_client):
    response = test_client.get('api/v1/tasks')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert 'tasks' in response.json


def test_create_and_get_task(test_client):
    board_id = create_test_board(test_client)
    task_data = {'text': 'Test Task', 'board_id': board_id}
    create_response = test_client.post('api/v1/tasks', json=task_data)
    assert create_response.status_code == 201
    task_id = create_response.json['task']['id']

    get_response = test_client.get(f'api/v1/tasks/{task_id}')
    assert get_response.status_code == 200
    assert get_response.json['task']['id'] == task_id
    assert get_response.json['task']['board_id'] == board_id


def test_update_task_status(test_client):
    board_id = create_test_board(test_client)
    task_data = {'text': 'Test Task', 'board_id': board_id}
    create_response = test_client.post('api/v1/tasks', json=task_data)
    task_id = create_response.json['task']['id']

    updated_data = {'status': True}
    update_response = test_client.put(f'api/v1/tasks/{task_id}/status', json=updated_data)
    assert update_response.status_code == 200


def test_delete_task(test_client):
    board_id = create_test_board(test_client)
    task_data = {'text': 'Test Task', 'board_id': board_id}
    create_response = test_client.post('api/v1/tasks', json=task_data)
    task_id = create_response.json['task']['id']

    delete_response = test_client.delete(f'api/v1/tasks/{task_id}')
    assert delete_response.status_code == 200
