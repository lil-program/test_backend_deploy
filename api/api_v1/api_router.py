from api.api_v1.endpoints import closets, clothes, test, users
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(closets.router, prefix="/closets", tags=["closets"])
api_router.include_router(clothes.router, prefix="/clothes", tags=["clothes"])

api_router.include_router(test.router, prefix="/test", tags=["test"])
