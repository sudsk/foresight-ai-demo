"""
FastAPI server for Master Orchestrator
"""
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agents.orchestrator.agent import MasterOrchestrator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Master Orchestrator API")
orchestrator = MasterOrchestrator()


class OrchestratorRequest(BaseModel):
    """Request model"""
    message: str
    session_id: str = "default"


class OrchestratorResponse(BaseModel):
    """Response model"""
    response: str
    session_id: str


@app.post("/orchestrate", response_model=OrchestratorResponse)
async def orchestrate(request: OrchestratorRequest):
    """Process request via orchestrator"""
    try:
        response_text = await orchestrator.process(
            request.message,
            request.session_id
        )
        
        return OrchestratorResponse(
            response=response_text,
            session_id=request.session_id
        )
    except Exception as e:
        logger.error(f"Orchestration error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    """Health check"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
