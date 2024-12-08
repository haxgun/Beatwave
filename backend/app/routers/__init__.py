from fastapi import APIRouter

from app.routers import token

api_router = APIRouter()
api_router.include_router(token.router, prefix="/token", tags=["token"])