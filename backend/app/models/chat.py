"""Chat data models"""
from pydantic import BaseModel, Field
from typing import Literal


class ChatMessage(BaseModel):
    """Chat message"""
    id: str = Field(..., description="Message ID")
    role: Literal["user", "assistant"] = Field(..., description="Message role")
    content: str = Field(..., description="Message content")
    timestamp: str = Field(..., description="Message timestamp")


class ChatRequest(BaseModel):
    """Chat request"""
    message: str = Field(..., description="User message")
