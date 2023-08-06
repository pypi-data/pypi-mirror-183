from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import APIRouter, Depends
# from core.helpers.cache import Cache
# from core.schemas import CommonParams
# from ..exceptions import SampleError
# from ..schemas.request import ReqUserLogin, ReqForgotPassword
# from ..schemas.response import ResLogin, ResMe
# from ..services.core_auth_service import CoreAuthService
# from ..jobs import TASK_UPDATE
from sequoia.libs.auth import Authenticated
from ..permission import AUTH_ME
limiter = Limiter(key_func=get_remote_address)

router = APIRouter(dependencies=[Depends(AUTH_ME)])
# router = APIRouter()


@router.get("/me")
async def gme(userid=Depends(Authenticated.user_id)):

    # to db
    # print("userid", userid)

    return {
        "as": 903284
    }


# @router.post("/update")
# async def update_profile(
#         data: ReqForgotPassword,
#         bt: BackgroundTasks,
#         request: Request):

#     # to db
#     await CoreAuthService().find_by_email(data.email)

#     # task
#     bt.add_task(TASK_UPDATE(), data.__dict__)

#     return {}


# @router.put("/{id}")
# async def update_user(id: int, data: dict, bt: BackgroundTasks):

#     # to db
#     await CoreAuthService().update_user(id, data)

#     # task
#     bt.add_task(TASK_UPDATE(), {"id": id})

#     return True


# @router.get("/{id}")
# async def get_user(id: int, request: Request):

#     @Cache(ttl=45, request=request)
#     async def crut():
#         return await CoreAuthService().get_user(id)

#     return await crut()


# @router.delete("/{id}")
# async def delete_user(id: int, bt: BackgroundTasks):

#     d = await CoreAuthService().delete_user(id)

#     # task
#     bt.add_task(TASK_UPDATE(), {"id": id})

#     return d
