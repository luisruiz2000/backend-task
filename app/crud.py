from datetime import datetime
from typing import Optional, List
import uuid

class Task:
    def __init__(self, title: str, description: Optional[str] = None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.completed = False

tasks: List[Task] = []

def get_all_tasks():
    return [task_to_dict(task) for task in tasks]

def create_task(title: str, description: Optional[str] = None):
    task = Task(title, description)
    tasks.append(task)
    return task_to_dict(task)

def update_task_completed(task_id: str, completed: bool):
    for task in tasks:
        if task.id == task_id:
            task.completed = completed
            return {
                "message": f"Se actualizó el estado de la tarea '{task.title}' a {'completada' if completed else 'no completada'}.",
                "task": task_to_dict(task)
            }
    return None

def delete_task(task_id: str):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            deleted_title = task.title
            tasks.pop(i)
            return {"message": f"Se eliminó la tarea '{deleted_title}' correctamente."}
    return None

def task_to_dict(task: Task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "created_at": task.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "completed": task.completed
    }
