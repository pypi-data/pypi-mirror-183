# import requests
from typing import Any
from sqlalchemy import select
from datetime import datetime, timedelta
from sequoia.libs.worker.task import TASK
from ..models import CoreUsersAccounts


class ping(TASK):
    session: Any
    msg_id: str
    module: str
    taskname: str
    data: dict

    async def __call__(self):

        try:
            s = select(CoreUsersAccounts).limit(2)
            result = self.session.execute(s)
            cts = result.scalars().all()
            for t in cts:
                print('xxx', t.fullname)

        except Exception as e:
            print(e)

        # Now with some filter
        now = datetime.now()
        ss = now - timedelta(minutes=10)
        print('older', now, ss)
        stmt = (
            select(CoreUsersAccounts).
            filter(CoreUsersAccounts.created_at <= ss).limit(2)
        )
        t = self.session.execute(stmt)
        ctss = t.scalars().all()
        for t in ctss:
            print('sss', t)

        # set completed task
        await self.completed({"conclusion": "success"})
