import pytest
from sqlalchemy import select
from sqlalchemy.orm import lazyload

from app.models.task import Task
from app.models.board import Board, BoardStatus
from app import db


def test_task_creation(test_app):
    with test_app.app_context():
        board = Board(status=BoardStatus.OPEN.value)
        db.session.add(board)
        db.session.commit()

        task = Task(text="Test Task", board_id=board.id, is_completed=False)
        db.session.add(task)
        db.session.commit()

        saved_task = db.session.scalars(select(Task).where(Task.id == task.id)).first()
        assert saved_task.text == "Test Task"
        assert saved_task.is_completed is False
        assert saved_task.board_id == board.id


def test_task_update(test_app):
    with test_app.app_context():
        board = Board(status=BoardStatus.OPEN.value)
        db.session.add(board)
        db.session.commit()

        task = Task(text="Test Task", board_id=board.id)
        db.session.add(task)
        db.session.commit()

        task.text = "Updated Test Task"
        db.session.commit()

        updated_task = db.session.scalars(select(Task).where(Task.id == task.id)).first()
        assert updated_task.text == "Updated Test Task"


def test_task_deletion(test_app):
    with test_app.app_context():
        board = Board(status=BoardStatus.OPEN.value)
        db.session.add(board)
        db.session.commit()

        task = Task(text="Test Task", board_id=board.id)
        db.session.add(task)
        db.session.commit()

        db.session.delete(task)
        db.session.commit()

        deleted_task = db.session.scalars(select(Task).where(Task.id == task.id)).first()
        assert deleted_task is None


def test_task_relationship(test_app):
    with test_app.app_context():
        board = Board(status=BoardStatus.OPEN.value)
        db.session.add(board)
        db.session.commit()

        task = Task(text="Test Task", board_id=board.id)
        db.session.add(task)
        db.session.commit()

        saved_task = db.session.scalars(select(Task).where(Task.id == task.id).options(lazyload(Task.board))).first()
        assert saved_task.board.id == board.id
        assert saved_task.board.status == BoardStatus.OPEN.value
