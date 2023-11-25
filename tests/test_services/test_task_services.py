import pytest
from app.models.board import Board, BoardStatus
from app.models.task import Task
from app.services.task_service import TaskService
from app import db


def create_test_board():
    new_board = Board(status=BoardStatus.OPEN.value)
    db.session.add(new_board)
    db.session.commit()
    return new_board


def test_create_and_get_task(test_app):
    with test_app.app_context():
        test_board = create_test_board()
        task_data = {'text': 'Test Task', 'board_id': test_board.id}
        create_response = TaskService.create_task(task_data)
        assert create_response.status_code == 201
        task_id = create_response.json['task']['id']

        get_response = TaskService.get_task_by_id(task_id)
        assert get_response.status_code == 200
        assert get_response.json['task']['id'] == task_id


def test_update_task_status(test_app):
    with test_app.app_context():
        test_board = create_test_board()
        task_data = {'text': 'Test Task', 'board_id': test_board.id}
        create_response = TaskService.create_task(task_data)
        task_id = create_response.json['task']['id']

        update_response = TaskService.update_task_status(task_id, True)
        assert update_response.status_code == 200

        get_response = TaskService.get_task_by_id(task_id)
        assert get_response.json['task']['is_completed'] is True


def test_delete_task(test_app):
    with test_app.app_context():
        test_board = create_test_board()
        task_data = {'text': 'Test Task', 'board_id': test_board.id}
        create_response = TaskService.create_task(task_data)
        task_id = create_response.json['task']['id']

        delete_response = TaskService.delete_task(task_id)
        assert delete_response.status_code == 200

        get_response = TaskService.get_task_by_id(task_id)
        assert get_response.status_code == 404
