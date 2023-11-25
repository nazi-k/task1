import pytest
from app.models.board import BoardStatus
from app.services.board_service import BoardService


def test_create_and_get_board(test_app):
    with test_app.app_context():
        create_response = BoardService.create_board()
        assert create_response.status_code == 201
        board_id = create_response.json['board']['id']

        get_response = BoardService.get_board_by_id(board_id)
        assert get_response.status_code == 200
        assert get_response.json['board']['id'] == board_id


def test_update_board_status(test_app):
    with test_app.app_context():
        create_response = BoardService.create_board()
        board_id = create_response.json['board']['id']

        update_response = BoardService.update_board_status(board_id, BoardStatus.ARCHIVED)
        assert update_response.status_code == 200

        get_response = BoardService.get_board_by_id(board_id)
        assert get_response.json['board']['status'] == BoardStatus.ARCHIVED.value
