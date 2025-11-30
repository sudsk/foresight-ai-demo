"""
Scenarios API endpoints
"""
from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import List
from pydantic import BaseModel
from app.models.scenario import Scenario
from app.services.scenario_service import ScenarioService

router = APIRouter()
scenario_service = ScenarioService()


class CreateScenarioRequest(BaseModel):
    description: str


@router.get("/", response_model=List[Scenario])
async def get_scenarios():
    """Get all scenarios"""
    return scenario_service.get_all_scenarios()


@router.post("/", response_model=Scenario)
async def create_scenario(
    request: CreateScenarioRequest,
    background_tasks: BackgroundTasks
):
    """Create and run new scenario"""
    scenario = scenario_service.create_scenario(request.description)
    
    # Run scenario processing in background
    background_tasks.add_task(
        scenario_service.process_scenario,
        scenario.id
    )
    
    return scenario


@router.get("/{scenario_id}", response_model=Scenario)
async def get_scenario(scenario_id: str):
    """Get specific scenario by ID"""
    scenario = scenario_service.get_scenario_by_id(scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail=f"Scenario {scenario_id} not found")
    return scenario


@router.delete("/{scenario_id}")
async def delete_scenario(scenario_id: str):
    """Delete scenario"""
    success = scenario_service.delete_scenario(scenario_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Scenario {scenario_id} not found")
    return {"message": "Scenario deleted successfully"}
