from typing import Any
from sqlalchemy import select, or_, func
from dataclasses import dataclass
from sqlalchemy.orm import selectinload
from core.db.queries import BaseQuery
from ..models import MainTasks
from ..schemas.request import ReqUserCreate


@dataclass
class CoreMainService(BaseQuery):

    # db model
    model: Any = MainTasks

    async def find_user(self):
        """default paginate search"""

        # filter
        fltr = or_(
            self.model.fullname.ilike(f"%{self.params.q}%"),
            self.model.email.ilike(f"%{self.params.q}%"),
        )

        # ---------------
        # query untuk search
        # # .filter(self.model.role == 'admin') \
        # ---------------
        if self.params.q:
            query = select(self.model) \
                .filter(fltr) \
                .options(selectinload(self.model.alamat))
        else:
            query = select(self.model) \
                .options(selectinload(self.model.alamat))

        # ---------------
        # count with filter
        # ---------------
        if self.params.q:
            ss = select(func.count(self.model.id)) \
                .filter(fltr)
        else:
            ss = select(func.count(self.model.id))

        count = await self.count(ss)

        return {
            "count": count,
            "results": await self.find(query)
        }

    async def create_user(self, data: ReqUserCreate):
        """inserting new data"""
        await self.insert(data)
        return {
            "insert": True
        }

    async def update_user(self, id: int, data: dict):
        """update user"""
        await self.update(id, data)
        return {
            "update": True
        }

    async def get_user(self, id: int):
        """Detail by id"""

        query = select(self.model) \
            .filter(self.model.id == id) \
            .options(selectinload(self.model.alamat))

        return await self.find_one(query)

    async def delete_user(self, id: int):
        """Delete service"""

        await self.delete(id)
        return {
            "delete": True
        }
