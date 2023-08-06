import os
from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from sequoia.libs.notify import NotifySlack
from sequoia.core.modules import get_modules
from sequoia.core.exceptions import CustomException


def init_listeners(app_: FastAPI) -> None:
    # Exception handler
    app_.add_middleware(GZipMiddleware, minimum_size=1000)

    @app_.on_event("startup")
    async def startup_event():

        c = NotifySlack()
        await c.send_slack("Ignite start")
        await get_modules()

    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

    @app_.middleware("http")
    async def add_process_time_header(request: Request, call_next):

        os.environ["SCHEMA"] = request.headers['host'].replace(
            ".", "_")

        # print('middle x', call_next)
        response = await call_next(request)
        return response
