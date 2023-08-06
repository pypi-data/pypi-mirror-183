from fastapi import APIRouter
from .core_users_route import router as core_users_route

router = APIRouter()
router.include_router(core_users_route)
