from .v1 import board_route, task_route

from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1.register_blueprint(task_route)
api_v1.register_blueprint(board_route)
