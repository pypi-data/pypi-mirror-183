from fastapi import APIRouter
from .core_auth_route import router as core_auth_route
from .core_auth_loggedin import router as core_auth_loggedin

router = APIRouter()
router.include_router(core_auth_route)
router.include_router(core_auth_loggedin)
