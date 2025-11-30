"""
Application configuration
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "Foresight AI Backend"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
    ]
    
    # Google Cloud
    GCP_PROJECT_ID: str = "foresight-ai-demo"
    VERTEX_AI_LOCATION: str = "europe-west2"
    GEMINI_MODEL: str = "gemini-2.0-flash-exp"
    
    # Agent URLs
    AGENT_ORCHESTRATOR_URL: str = "http://localhost:8080"
    MCP_SERVER_URL: str = "http://localhost:8001"
    
    # WebSocket
    WS_HEARTBEAT_INTERVAL: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
