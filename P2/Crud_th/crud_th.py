from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

tasks_db = []

# --- THE MODEL ---
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool = False

# --- 1. CREATE (POST) ---
@app.post("/tasks/", status_code=201, response_model=Task)
def create_task(task: Task):
    # Check if ID already exists
    for t in tasks_db:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Task ID already exists")
    
    tasks_db.append(task)
    return task

# --- 2. READ ALL (GET) ---
@app.get("/tasks/", response_model=List[Task])
def get_all_tasks():
    return tasks_db

# --- 3. READ ONE (GET) ---
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# --- 4. UPDATE (PUT) ---
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[i] = updated_task
            return updated_task
            
    raise HTTPException(status_code=404, detail="Task not found")

# --- 5. DELETE (DELETE) ---
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return
            
    raise HTTPException(status_code=404, detail="Task not found")
