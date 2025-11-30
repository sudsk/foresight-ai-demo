"""
Tasks API endpoints
"""
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.task import Task
from app.services.task_service import TaskService

router = APIRouter()
task_service = TaskService()


@router.get("/", response_model=List[Task])
async def get_tasks():
    """Get all tasks"""
    return task_service.get_all_tasks()


@router.post("/", response_model=Task)
async def create_task(task: Task):
    """Create new task"""
    return task_service.create_task(task)


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: str):
    """Get specific task by ID"""
    task = task_service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return task


@router.patch("/{task_id}", response_model=Task)
async def update_task(task_id: str, updates: dict):
    """Update task"""
    task = task_service.update_task(task_id, updates)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return task


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    """Delete task"""
    success = task_service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return {"message": "Task deleted successfully"}


@router.post("/{task_id}/complete", response_model=Task)
async def complete_task(task_id: str):
    """Mark task as complete"""
    task = task_service.complete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return task
