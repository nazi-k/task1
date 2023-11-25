from sqlalchemy import select, update

from app import db
from app.models.board import Board, BoardStatus

from flask import make_response, Response


class BoardService:
    @staticmethod
    def get_boards(status: BoardStatus | None = None) -> Response:
        query = select(Board)

        if status is not None:
            query = query.where(Board.status == status.value)

        boards = db.session.scalars(query).all()
        return make_response({'boards': [board.to_dict() for board in boards]}, 200)

    @staticmethod
    def get_board_by_id(board_id: str) -> Response:
        board = db.session.scalars(select(Board).where(Board.id == board_id)).first()
        return make_response({'board': board.to_dict()}, 200) if board \
            else make_response({'message': 'Board not found'}, 404)

    @staticmethod
    def create_board() -> Response:
        new_board = Board()
        db.session.add(new_board)
        db.session.commit()
        return make_response({'board': new_board.to_dict()}, 201)

    @staticmethod
    def update_board_status(board_id: str, status: BoardStatus) -> Response:
        stmt = (
            update(Board).
            where(Board.id == board_id).
            values(status=status.value)
        )
        result = db.session.execute(stmt)
        if result.rowcount > 0:
            return make_response({'message': 'Board updated successfully'}, 200)
        else:
            return make_response({'message': 'Board not found'}, 404)
