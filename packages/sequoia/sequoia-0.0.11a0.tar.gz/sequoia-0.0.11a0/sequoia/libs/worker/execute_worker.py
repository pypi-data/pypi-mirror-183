import ujson
from typing import Any
from pydoc import locate
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import update
from modules.core_main.models import MainTasks
from core.logger import logger


@dataclass
class CrotJob:
    session: Any
    msg_id: str
    module: str
    taskname: str
    data: dict

    async def completed(self, data: dict):
        """set task complete after job kelar"""

        data["status"] = "completed"
        data["updated_at"] = datetime.now()
        if "conclusion" not in data:
            data["conclusion"] = "failed"

        stmt = (
            update(MainTasks).
            where(MainTasks.id == self.msg_id).
            values(data)
        )
        try:
            self.session.execute(stmt)
            self.session.commit()
        except Exception as e:
            print(e)

    async def __call__(self):
        kelas = locate(f"modules.{self.module}.tasks.{self.taskname}")
        try:
            s = getattr(kelas, '__call__')
            await s(self)
        except Exception:

            logger.info(f"task not found: {self.module} - {self.taskname}")
            # logger.info(e)

            await self.completed({
                "conclusion": "failed",
                "msg": "task not found"
            })


@dataclass
class ExecuteJob:
    session: Any

    @staticmethod
    def finish(msg_id: str, completed: bool = False, data: dict = {}):
        print('kopets', msg_id, completed, data)

    async def load_class(self, module: str, taskname: str, msg_id: str, data):
        c = CrotJob(session=self.session, msg_id=msg_id,
                    module=module, taskname=taskname, data=data)
        await c()

    async def do_task(self, srcdat):
        module = srcdat.attributes["module"]
        taskname = srcdat.attributes["taskname"]
        msg_id = srcdat.message_id
        data = ujson.loads(srcdat.data.decode("utf-8")) or {}

        try:
            await self.load_class(module, taskname, msg_id, data)
        except Exception as e:
            print('err', e)
