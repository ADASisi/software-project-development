from app.models.task import Task
from app import db

class TaskService:
    @staticmethod
    def create_task(data):
        task = Task(**data)
        db.session.add(task)
        db.session.commit()
        return task.serialize()

    @staticmethod
    def get_all_tasks():
        tasks = Task.query.all()
        return [task.serialize() for task in tasks]