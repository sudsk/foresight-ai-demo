"""Scenario data models"""
from pydantic import BaseModel, Field
from typing import Optional, Literal, List
from datetime import datetime


class ScenarioResults(BaseModel):
    """Scenario analysis results"""
    portfolio_impact: dict = Field(..., description="Portfolio-level impact")
    sector_impact: List[dict] = Field(..., description="Impact by sector")
    top_impacted: List[dict] = Field(..., description="Most impacted SMEs")


class Scenario(BaseModel):
    """Scenario entity"""
    id: str = Field(..., description="Scenario ID")
    name: str = Field(..., description="Scenario name/description")
    status: Literal["in_progress", "completed"] = Field(..., description="Scenario status")
    progress: Optional[int] = Field(None, ge=0, le=100, description="Progress percentage")
    duration: Optional[int] = Field(None, description="Duration in seconds")
    created_at: str = Field(..., description="Creation timestamp")
    completed_at: Optional[str] = Field(None, description="Completion timestamp")
    results: Optional[ScenarioResults] = Field(None, description="Scenario results")
