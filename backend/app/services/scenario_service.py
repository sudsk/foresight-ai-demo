"""
Scenario service - scenario simulation logic
"""
from typing import List, Optional
from datetime import datetime
import asyncio
import time
from app.models.scenario import Scenario, ScenarioResults
from app.api.v1.websocket import broadcast_update


class ScenarioService:
    """Scenario simulation service"""
    
    def __init__(self):
        # In-memory storage for demo
        self._scenarios: List[Scenario] = []
        self._generate_mock_scenarios()
    
    def get_all_scenarios(self) -> List[Scenario]:
        """Get all scenarios"""
        return self._scenarios
    
    def get_scenario_by_id(self, scenario_id: str) -> Optional[Scenario]:
        """Get scenario by ID"""
        return next((s for s in self._scenarios if s.id == scenario_id), None)
    
    def create_scenario(self, description: str) -> Scenario:
        """Create new scenario"""
        scenario_id = f"scenario_{int(time.time() * 1000)}"
        
        scenario = Scenario(
            id=scenario_id,
            name=description,
            status="in_progress",
            progress=0,
            duration=None,
            created_at=datetime.utcnow().isoformat() + "Z",
            completed_at=None,
            results=None
        )
        
        self._scenarios.insert(0, scenario)
        return scenario
    
    async def process_scenario(self, scenario_id: str):
        """
        Process scenario in background
        Simulates ML model running across 1,284 SMEs
        """
        scenario = self.get_scenario_by_id(scenario_id)
        if not scenario:
            return
        
        start_time = time.time()
        
        # Simulate processing with progress updates
        for progress in range(0, 101, 10):
            await asyncio.sleep(1.5)  # Simulate processing time
            
            # Update progress
            scenario.progress = progress
            
            # Broadcast progress update via WebSocket
            await broadcast_update("scenario_update", {
                "id": scenario.id,
                "progress": progress,
                "status": "in_progress"
            })
        
        # Calculate duration
        duration = int(time.time() - start_time)
        
        # Generate mock results
        results = self._generate_mock_results(scenario.name)
        
        # Update scenario to completed
        scenario.status = "completed"
        scenario.progress = 100
        scenario.duration = duration
        scenario.completed_at = datetime.utcnow().isoformat() + "Z"
        scenario.results = results
        
        # Broadcast completion
        await broadcast_update("scenario_update", {
            "id": scenario.id,
            "status": "completed",
            "duration": duration,
            "results": results.dict()
        })
    
    def delete_scenario(self, scenario_id: str) -> bool:
        """Delete scenario"""
        scenario = self.get_scenario_by_id(scenario_id)
        if scenario:
            self._scenarios.remove(scenario)
            return True
        return False
    
    def _generate_mock_results(self, scenario_name: str) -> ScenarioResults:
        """Generate mock scenario results"""
        # Customize results based on scenario type
        if "interest rate" in scenario_name.lower() or "rate" in scenario_name.lower():
            return ScenarioResults(
                portfolio_impact={
                    "critical_before": 23,
                    "critical_after": 38,
                    "default_prob_before": 2.8,
                    "default_prob_after": 4.2,
                    "avg_score_before": 64,
                    "avg_score_after": 68
                },
                sector_impact=[
                    {"sector": "Construction", "smes": 8, "avg_change": 8},
                    {"sector": "Retail", "smes": 12, "avg_change": 6},
                    {"sector": "Manufacturing", "smes": 5, "avg_change": 4}
                ],
                top_impacted=[
                    {
                        "sme_id": "#0234",
                        "sme_name": "BuildCo Construction",
                        "score_before": 72,
                        "score_after": 86,
                        "change": 14,
                        "reason": "High debt service burden with variable rates"
                    },
                    {
                        "sme_id": "#0456",
                        "sme_name": "Retail Fashion Group",
                        "score_before": 68,
                        "score_after": 81,
                        "change": 13,
                        "reason": "Increased financing costs on inventory"
                    }
                ]
            )
        elif "hemp" in scenario_name.lower() or "ban" in scenario_name.lower():
            return ScenarioResults(
                portfolio_impact={
                    "critical_before": 23,
                    "critical_after": 25,
                    "default_prob_before": 2.8,
                    "default_prob_after": 3.1,
                    "avg_score_before": 64,
                    "avg_score_after": 66
                },
                sector_impact=[
                    {"sector": "Food/Hospitality", "smes": 8, "avg_change": 15},
                    {"sector": "Retail", "smes": 4, "avg_change": 8}
                ],
                top_impacted=[
                    {
                        "sme_id": "#0445",
                        "sme_name": "GreenLeaf Products",
                        "score_before": 72,
                        "score_after": 87,
                        "change": 15,
                        "reason": "Revenue drop due to product ban"
                    },
                    {
                        "sme_id": "#0672",
                        "sme_name": "Natural Wellness Ltd",
                        "score_before": 68,
                        "score_after": 82,
                        "change": 14,
                        "reason": "Market contraction impact"
                    }
                ]
            )
        else:
            # Generic scenario results
            return ScenarioResults(
                portfolio_impact={
                    "critical_before": 23,
                    "critical_after": 28,
                    "default_prob_before": 2.8,
                    "default_prob_after": 3.4,
                    "avg_score_before": 64,
                    "avg_score_after": 67
                },
                sector_impact=[
                    {"sector": "Software/Technology", "smes": 12, "avg_change": 5},
                    {"sector": "Retail", "smes": 8, "avg_change": 7},
                    {"sector": "Manufacturing", "smes": 6, "avg_change": 4}
                ],
                top_impacted=[
                    {
                        "sme_id": "#0142",
                        "sme_name": "TechStart Solutions",
                        "score_before": 68,
                        "score_after": 78,
                        "change": 10,
                        "reason": "Generic scenario impact"
                    }
                ]
            )
    
    def _generate_mock_scenarios(self):
        """Generate mock completed scenarios for demo"""
        # Add one completed scenario
        completed = Scenario(
            id="scenario_001",
            name="UK Hemp Products Ban Impact",
            status="completed",
            progress=100,
            duration=18,
            created_at="2024-11-15T14:30:00Z",
            completed_at="2024-11-15T14:30:18Z",
            results=ScenarioResults(
                portfolio_impact={
                    "critical_before": 23,
                    "critical_after": 25,
                    "default_prob_before": 2.8,
                    "default_prob_after": 3.1,
                    "avg_score_before": 64,
                    "avg_score_after": 66
                },
                sector_impact=[
                    {"sector": "Food/Hospitality", "smes": 8, "avg_change": 15}
                ],
                top_impacted=[
                    {
                        "sme_id": "#0445",
                        "sme_name": "GreenLeaf Products",
                        "score_before": 72,
                        "score_after": 87,
                        "change": 15,
                        "reason": "Revenue drop due to product ban"
                    }
                ]
            )
        )
        self._scenarios.append(completed)
