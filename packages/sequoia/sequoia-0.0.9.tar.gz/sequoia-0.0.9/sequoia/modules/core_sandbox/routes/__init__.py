from fastapi import APIRouter
from sequoia.modules.core_sandbox.routes.sandbox import router as sandbox_route

router = APIRouter()
router.include_router(sandbox_route)
