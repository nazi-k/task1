from flask import Blueprint, jsonify, request
from app.services.task_service import TaskService

task_route = Blueprint('task_view', __name__)


@task_route.route('/tasks', methods=['GET'])
def get_tasks():
    is_completed = request.args.get('is_completed', default=None, type=bool)
    board_id = request.args.get('board_id', default=None, type=str)
    return TaskService.get_tasks(is_completed, board_id)


@task_route.route('/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id: str):
    return TaskService.get_task_by_id(task_id)


@task_route.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'text' not in data or 'board_id' not in data:
        return jsonify({'message': 'Missing required data'}), 400
    return TaskService.create_task(data)


@task_route.route('/tasks/<string:task_id>/status', methods=['PUT'])
def update_task_status(task_id):
    data = request.get_json()
    return TaskService.update_task_status(task_id, data.get('status'))


@task_route.route('/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return TaskService.delete_task(task_id)
