from fastapi import FastAPI
from .routes import router


def init_app():
    app = FastAPI()
    app.include_router(router)
    return app


app = init_app()
