"""
API routes aggregator
"""
from fastapi import APIRouter
from app.api.v1 import portfolio, scenarios, tasks, news, chat, activities

api_router = APIRouter()

# Include v1 routes
api_router.include_router(
    portfolio.router,
    prefix="/v1/portfolio",
    tags=["portfolio"]
)

api_router.include_router(
    scenarios.router,
    prefix="/v1/scenarios",
    tags=["scenarios"]
)

api_router.include_router(
    tasks.router,
    prefix="/v1/tasks",
    tags=["tasks"]
)

api_router.include_router(
    news.router,
    prefix="/v1/news",
    tags=["news"]
)

api_router.include_router(
    chat.router,
    prefix="/v1/chat",
    tags=["chat"]
)

api_router.include_router(
    activities.router,
    prefix="/v1/activities",
    tags=["activities"]
)
