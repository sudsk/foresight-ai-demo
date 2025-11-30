"""
Chat API endpoints
"""
from fastapi import APIRouter
from typing import List
from app.models.chat import ChatMessage, ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()


@router.post("/message", response_model=ChatMessage)
async def send_message(request: ChatRequest):
    """Send message to AI assistant"""
    return await chat_service.process_message(request.message)


@router.get("/history", response_model=List[ChatMessage])
async def get_chat_history():
    """Get chat history"""
    return chat_service.get_history()
