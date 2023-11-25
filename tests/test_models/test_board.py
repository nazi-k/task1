import pytest
from sqlalchemy import select
from sqlalchemy.orm import lazyload

from app.models.board import Board, BoardStatus
from app.models.task import Task
from app import db


def test_board_creation(test_app):
    with test_app.app_context():
        board = Board(status=BoardStatus.OPEN.value)
        db.session.add(board)
        db.session.commit()

        saved_board = db.session.scalars(select(Board).where(Board.id == Board.id)).first()
        assert saved_board.status == BoardStatus.OPEN.value


def test_board_update(test_app):
    with test_app.app_context():
        board = Board(status=BoardStatus.OPEN.value)
        db.session.add(board)
        db.session.commit()

        board.status = BoardStatus.ARCHIVED.value
        db.session.commit()

        updated_board = db.session.scalars(select(Board).where(Board.id == board.id)).first()
        assert updated_board.status == BoardStatus.ARCHIVED.value


def test_board_relationship(test_app):
    with test_app.app_context():
        board = Board(status=BoardStatus.OPEN.value)
        db.session.add(board)
        db.session.commit()

        task = Task(text="Test Task", board_id=board.id)
        db.session.add(task)
        db.session.commit()

        saved_board = db.session.scalars(
            select(Board).where(Board.id == board.id).options(lazyload(Board.tasks))
        ).first()
        assert saved_board.tasks[0].text == "Test Task"
