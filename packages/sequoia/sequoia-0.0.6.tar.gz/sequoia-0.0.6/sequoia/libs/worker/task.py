from dataclasses import dataclass
from abc import ABC
from typing import Any


@dataclass
class TASK(ABC):
    session: Any
    msg_id: str
    module: str
    taskname: str
    data: dict

    async def completed(self, msg: dict):
        ...

    async def __call__(self):
        ...
        await self.completed({"conclusion": "success"})
