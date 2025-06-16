from fastapi import FastAPI, HTTPException
from typing import Optional
from app.crud import get_all_tasks, create_task, update_task_completed, delete_task
from app.models import CreateTaskModel

app = FastAPI()

@app.get("/tasks")
def get_tasks():
    tasks = get_all_tasks()
    if not tasks:
        return {"message": "¡No tienes tareas aún! Agrega tu nueva tarea o meta para comenzar."}
    return {"tasks": tasks}

@app.post("/tasks")
def create_task_endpoint(task: CreateTaskModel):
    task_dict = create_task(task.title, task.description)
    return {"task": task_dict}

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: str):
    result = delete_task(task_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.put("/tasks/{task_id}")
def update_task_completed_endpoint(task_id: str, completed: bool):
    result = update_task_completed(task_id, completed)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Tarea no encontrada")