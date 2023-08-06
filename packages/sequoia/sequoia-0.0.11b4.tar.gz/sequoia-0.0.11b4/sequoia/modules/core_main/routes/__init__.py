from fastapi import APIRouter
from .core_main_route import router as core_main_route

router = APIRouter()
router.include_router(core_main_route)
