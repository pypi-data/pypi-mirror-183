import ujson
import asyncio
import aioredis
import inspect
from datetime import datetime
from sequoia.core.config import config


class JOBTASK(Exception):
    taskname: str = "~taskname~"
    log: bool = False

    async def main(self, module: str, data: dict):

        # redis connect
        redis = aioredis.from_url(
            url=f"{config.REDIS.MAIN.URI}",
            encoding="utf-8",
            decode_responses=True
        )

        await redis.lpush('_queues', ujson.dumps({
            "module": module,
            "taskname": self.taskname,
            "log": self.log,
            "datetime": int(round(datetime.now().timestamp())),
            "data": data,
            # "account_id": 1
        }))

        # DevOnly
        # logger.info(f"Add rdtask: {stask}")

    def __call__(self, data: dict):
        module = str(f"{inspect.getmodule(self).__name__}").replace(
            "modules.", "").replace(".jobs", "")

        asyncio.run(self.main(module, data))


# class TASK_TEST(JOBTASK):
#     namespace = "sandbox"
#     subname = "login"
