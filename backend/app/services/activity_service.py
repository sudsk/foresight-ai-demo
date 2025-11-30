"""
Activity service - system activity logging
"""
from typing import List
from app.models.activity import Activity


class ActivityService:
    """System activity logging service"""
    
    def __init__(self):
        # Mock activities
        self._activities = self._generate_mock_activities()
    
    def get_all_activities(self) -> List[Activity]:
        """Get all system activities"""
        return self._activities
    
    def log_activity(self, activity_type: str, message: str):
        """Log new activity"""
        import time
        
        activity = Activity(
            id=f"act_{int(time.time() * 1000)}",
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            type=activity_type,
            message=message
        )
        self._activities.insert(0, activity)
    
    def _generate_mock_activities(self) -> List[Activity]:
        """Generate mock activity data"""
        return [
            Activity(
                id="act_001",
                timestamp="2024-11-16T14:32:17Z",
                type="alert",
                message="TechStart Solutions risk score increased to 68 (CRITICAL). CTO departure detected via LinkedIn."
            ),
            Activity(
                id="act_002",
                timestamp="2024-11-16T12:15:00Z",
                type="info",
                message="Q3 financial estimates batch updated for 1,284 SMEs. Average processing time: 23 seconds."
            ),
            Activity(
                id="act_003",
                timestamp="2024-11-16T10:45:32Z",
                type="success",
                message="Credit application #0823 GreenTech Energy approved at €300K facility."
            ),
            Activity(
                id="act_004",
                timestamp="2024-11-16T09:22:18Z",
                type="warning",
                message="Urban Fashion Ltd payment delays detected. 3 suppliers flagged (avg 47 days late)."
            ),
            Activity(
                id="act_005",
                timestamp="2024-11-16T08:10:45Z",
                type="info",
                message="Daily portfolio risk recalculation completed. 1,284 SMEs processed in 2 minutes."
            )
        ]
