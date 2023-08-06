from urllib.parse import urlparse
import ujson
from fastapi import APIRouter, Depends, Request  # BackgroundTasks
# from sequoia.core.fastapi.dependencies import PermissionDependency, IsPublic  # IsAdmin
from sequoia.core.helpers.cache import Cache
# from core.schemas import CommonParams
# from ..exceptions import SampleError
# from ..schemas.request import ReqUserCreate
# from ..schemas.response import ResUserCreate
# from ..services.core_main_service import CoreMainService
# from ..jobs import TASK_REGISTER, TASK_UPDATE, TASK_PING


router = APIRouter()


@router.get(
    "/",
)
async def home(request: Request):
    # @Cache(ttl=5)
    async def get_home():

        t = urlparse(request.url._url).netloc
        domain = '.'.join(t.split('.')[-2:])

        return {
            "status": "OK",
            "domain": domain,
            "codename": request.app.title
        }

    return await get_home()


@router.get(
    "/_cache",
)
async def get_cache_keys(request: Request):
    tsks = await Cache().keys("tasks")
    ac = []
    for k in tsks:
        m = await Cache().get(k)
        ac.append({
            "k": k,
            "v": ujson.loads(m)
        })
    return {
        "modules": await Cache().keys("module"),
        "tasks": ac
    }


# @router.get("/")
# async def home(request: Request, params=Depends(CommonParams)):

#     """Simple list users pagination"""

#     @Cache(ttl=5, request=request)
#     async def get_users():
#         """get data from db then caching"""
#         return await CoreMainService(params=params).find_user()

#     return await get_users()


# @router.post("/", response_model=ResUserCreate)
# async def create_users(data: ReqUserCreate, bt: BackgroundTasks):

#     # to db
#     await CoreMainService().create_user(data)

#     # task
#     bt.add_task(TASK_REGISTER(), data.__dict__)

#     return {"email": data.email}


# @router.get("/ping")
# async def ping_task(bt: BackgroundTasks):

#     # task
#     bt.add_task(TASK_PING(), {})

#     return {
#         "task": "ok"
#     }


# @router.get("/err")
# async def error_raise():

#     raise SampleError


# @router.put("/{id}")
# async def update_user(id: int, data: dict, bt: BackgroundTasks):

#     # to db
#     await CoreMainService().update_user(id, data)

#     # task
#     bt.add_task(TASK_UPDATE(), {"id": id})

#     return True


# @router.get("/{id}")
# async def get_user(id: int, request: Request):

#     @Cache(ttl=45, request=request)
#     async def crut():
#         return await CoreMainService().get_user(id)

#     return await crut()


# @router.delete("/{id}")
# async def delete_user(id: int, bt: BackgroundTasks):

#     d = await CoreMainService().delete_user(id)

#     # task
#     bt.add_task(TASK_UPDATE(), {"id": id})

#     return d
