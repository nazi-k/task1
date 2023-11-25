from sqlalchemy import select, delete, update

from app import db
from app.models.task import Task

from flask import make_response, Response


class TaskService:
    @staticmethod
    def get_tasks(is_completed: bool | None = None, board_id: str | None = None) -> Response:
        query = select(Task)

        if is_completed is not None:
            query = query.where(Task.is_completed == is_completed)

        if board_id is not None:
            query = query.where(Task.board_id == board_id)

        tasks = db.session.scalars(query).all()
        return make_response({'tasks': [task.to_dict() for task in tasks]}, 200)

    @staticmethod
    def get_task_by_id(task_id: str) -> Response:
        task = db.session.scalars(select(Task).where(Task.id == task_id)).first()
        return make_response({'task': task.to_dict()}, 200) if task \
            else make_response({'message': 'Task not found'}, 404)

    @staticmethod
    def create_task(data: dict) -> Response:
        new_task = Task(text=data['text'], board_id=data['board_id'])
        db.session.add(new_task)
        db.session.commit()
        return make_response({'task': new_task.to_dict()}, 201)

    @staticmethod
    def update_task_status(task_id: str, is_completed: bool) -> Response:
        stmt = (
            update(Task).
            where(Task.id == task_id).
            values(is_completed=is_completed)
        )
        result = db.session.execute(stmt)
        if result.rowcount > 0:
            return make_response({'message': 'Task updated successfully'}, 200)
        else:
            return make_response({'message': 'Task not found'}, 404)

    @staticmethod
    def delete_task(task_id: str) -> Response:
        result = db.session.execute(delete(Task).where(Task.id == task_id))
        if result.rowcount > 0:
            return make_response({'message': 'Task deleted successfully'}, 200)
        else:
            return make_response({'message': 'Task not found'}, 404)
