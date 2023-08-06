from fastapi import FastAPI


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="sequoia:pegasus",
        project="IkamaiIgnite",
        description="go bigger",
        version="1.0.0",
        openapi_url="/api/openapi.json",
        # dependencies=[Depends(Logging)],
        # docs_url=None if config.ENV == "prod" else "/api/docs",
        # redoc_url=None if config.ENV == "prod" else "/api/redoc",
        # middleware=make_middleware(),
    )

    # init_routers(app_=app_)
    # init_apps(app_=app_)
    # init_listeners(app_=app_)
    # init_cache()
    return app_


server = create_app()
