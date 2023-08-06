import sys
import os
from pydoc import locate
from fastapi import FastAPI, APIRouter
from sequoia.core.config import config
from sequoia.modules.core_main.routes import router as core_main
from sequoia.modules.core_sandbox.routes import router as core_sandbox
from sequoia.modules.core_auth.routes import router as core_auth
from sequoia.modules.core_users.routes import router as core_users

mod_dir = "/home/modules/"
if "MODULE_DIR" in os.environ:
    mod_dir = os.environ["MODULE_DIR"]

sys.path.append(mod_dir)


def app_route():
    route = APIRouter(prefix="/api", tags=["core"])
    route.include_router(core_main, tags=["core"])

    if config.ENV != "prod":
        route.include_router(core_sandbox, prefix="/sandbox", tags=["core"])

    route.include_router(core_auth, prefix="/auth", tags=["core"])
    route.include_router(core_users, prefix="/users", tags=["core"])

    if os.path.isdir(mod_dir):
        for file in os.listdir(mod_dir):
            d = os.path.join(mod_dir, file)
            if os.path.isdir(d):

                clsname = os.path.basename(d)
                kelas = locate(f"modules.{clsname}.routes")
                c = getattr(kelas, 'router')
                route.include_router(c)

    return route


def init_routers(app_: FastAPI) -> None:
    app_.include_router(app_route())
