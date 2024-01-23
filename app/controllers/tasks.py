from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = TaskService.create_task(data)
    return jsonify(task), 201

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = TaskService.get_all_tasks()
    return jsonify(tasks)

