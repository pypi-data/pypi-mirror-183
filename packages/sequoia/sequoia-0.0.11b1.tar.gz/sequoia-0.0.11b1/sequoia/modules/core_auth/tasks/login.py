# import requests
from typing import Any
from sequoia.libs.worker.task import TASK


async def kirim_email(taskname, data):
    print('kirim email bos', taskname, data)
    # requests.post(
    #     "https://hooks.slack.com/services/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", json={"text": data["awesome"]})


class login(TASK):
    session: Any
    msg_id: str
    module: str
    taskname: str
    data: dict

    async def __call__(self):
        await kirim_email(self.taskname, self.data)

        print(self.data)

        # set completed task
        await self.completed({"conclusion": "success", "user_id": self.data["id"]})
