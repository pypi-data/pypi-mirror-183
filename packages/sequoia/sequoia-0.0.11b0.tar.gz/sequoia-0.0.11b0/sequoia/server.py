from fastapi import FastAPI, Depends
from sequoia.core.fastapi.dependencies.logging import Logging
from sequoia.core.config import config
from sequoia.core.middleware import make_middleware
from sequoia.core.listeners import init_listeners
from sequoia.app.init_routers import init_routers
from sequoia.app.init_apps import init_apps
from sequoia.core.helpers.cache import Cache


def init_cache() -> None:
    Cache.init()


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="sequoia",
        project="IkamaiIgnite",
        description="go bigger",
        version="1.0.0",
        openapi_url="/api/openapi.json",
        dependencies=[Depends(Logging)],
        docs_url=None if config.ENV == "prod" else "/api/docs",
        redoc_url=None if config.ENV == "prod" else "/api/redoc",
        middleware=make_middleware(),
    )

    init_routers(app_=app_)
    init_apps(app_=app_)
    init_listeners(app_=app_)
    init_cache()
    return app_


server = create_app()
