# FastAPI REST API Starter Code
# Install FastAPI: pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: Define your Pydantic model for Task here
# Example:
# class Task(BaseModel):
#     id: int
#     title: str
#     description: str = ""
#     completed: bool = False

# In-memory storage for tasks
tasks = []

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to Task Management API"}

# TODO: Implement your API endpoints here
# GET /tasks - Get all tasks
# POST /tasks - Create a new task
# PUT /tasks/{task_id} - Update a task
# DELETE /tasks/{task_id} - Delete a task

# To run the server, use:
# uvicorn starter-code:app --reload
