from flask import Blueprint, request
from app.services.board_service import BoardService
from app.models.board import BoardStatus

board_route = Blueprint('board_view', __name__)


@board_route.route('/boards', methods=['GET'])
def get_boards():
    status = request.args.get('status', default=None, type=BoardStatus)
    return BoardService.get_boards(status)


@board_route.route('/boards/<string:board_id>', methods=['GET'])
def get_board(board_id: str):
    return BoardService.get_board_by_id(board_id)


@board_route.route('/boards', methods=['POST'])
def create_board():
    return BoardService.create_board()


@board_route.route('/boards/<string:board_id>/status', methods=['PUT'])
def update_board_status(board_id):
    data = request.get_json()
    try:
        new_status = BoardStatus(data.get('status'))
        return BoardService.update_board_status(board_id, new_status)
    except ValueError:
        return {'message': 'Invalid status'}, 400
