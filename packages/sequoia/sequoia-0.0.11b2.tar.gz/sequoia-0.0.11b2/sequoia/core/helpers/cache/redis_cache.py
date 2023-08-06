import hashlib
import ujson
from typing import Any
import inspect
from functools import wraps
from fastapi import Request
from sequoia.core.helpers.redis import redis
# import pickle


class Cache:
    def __init__(self,
                 prefix: str = "",
                 ttl: int = 360,
                 request: Request = Any
                 ):
        self.prefix = prefix
        self.ttl = ttl
        self.request = request

    @staticmethod
    def init():
        ...

    async def set(self, key, value):
        return await redis.set(key, value)

    async def get(self, key):
        return await redis.get(key)

    async def remove_all(self, key) -> None:
        ts = await redis.keys(f"{key}*")
        for t in ts:
            await redis.delete(t)
        return None

    async def keys(self, key: str):
        return await redis.keys(f"{key}*")

    def __call__(self, function):
        @wraps(function)
        async def decorator(*args, **kwargs):

            # generate key
            try:
                if self.request.query_params:
                    n = dict(self.request.query_params.items())
                    c = f"{self.request.url._url}_{n}"
                    ky = hashlib.sha256(c.encode()).hexdigest()
                else:
                    n = await self.request.json()
                    c = f"{self.request.url._url}_{n}"
                    ky = hashlib.sha256(c.encode()).hexdigest()
            except Exception:
                ky = function.__name__

            try:
                nmn = inspect.getmodule(function)
                # type: ignore
                key = f"{nmn.__name__}:{ky}"
                if self.prefix:
                    key = self.prefix
                t = await redis.get(key)
                if t:
                    # try:
                    #     rs = ujson.loads(t)
                    # except Exception as e:
                    #     print('ededd', e)
                    #     rs = pickle.loads(t)
                    # return rs
                    return ujson.loads(t)
                else:
                    result = await function(*args, **kwargs)
                    ress = ujson.dumps(result)
                    # if isinstance(result, dict):
                    #     ress = ujson.dumps(result)

                    # elif isinstance(result, object):
                    #     ress = pickle.dumps(result)

                    # save to redis
                    await redis.setex(
                        key,
                        self.ttl,
                        ress,
                    )
            except Exception as e:
                raise e

            return result

        return decorator
