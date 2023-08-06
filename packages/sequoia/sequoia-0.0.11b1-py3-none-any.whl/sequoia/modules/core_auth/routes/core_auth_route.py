from slowapi import Limiter
from slowapi.util import get_remote_address
from datetime import datetime
from fastapi import APIRouter, Request, BackgroundTasks
# from sequoia.core.helpers.cache import Cache
# from sequoia.core.schemas import CommonParams
from sequoia.libs.auth import Password
from ..exceptions import SampleError
from ..schemas.request import ReqUserLogin, ReqForgotPassword
from ..schemas.response import ResLogin
from ..services.core_auth_service import CoreAuthService
from ..jobs import TASK_FORGOT, TASK_LOGIN

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()


@router.post("/forgot-password")
@limiter.limit("2/minute")
async def create_users(
        data: ReqForgotPassword,
        bt: BackgroundTasks,
        request: Request):

    # to db
    await CoreAuthService().find_by_email(data.email)

    # task
    bt.add_task(TASK_FORGOT(), data.__dict__)

    return {}


@router.post("/login", response_model=ResLogin)
@limiter.limit("10/minute")
async def auth_login(
        data: ReqUserLogin,
        bt: BackgroundTasks,
        request: Request):

    # to db
    data_user = await CoreAuthService().find_by_email(data.email)

    # cek password
    user_token = Password().get_token(data.password, data_user)
    if user_token:

        data_user["token"] = user_token

        # update last login
        await CoreAuthService().update_user(data_user["id"], {
            "lastlogin": datetime.now()
        })

        # task
        bt.add_task(TASK_LOGIN(), data_user)
        return data_user
    else:
        raise SampleError


@router.get("/test")
async def get_all():
    # to db
    t = await CoreAuthService().find_user_by_id(1)
    return t


# @router.get("/schema")
# async def schema():
#     scm = await CoreAuthService().schema()
#     return scm
