from typing import Any
from sqlalchemy import select, or_, func
from dataclasses import dataclass
from sqlalchemy.orm import selectinload
from sequoia.core.db.queries import BaseQuery
from ..models import CoreAuthAccounts


@dataclass
class CoreAuthService(BaseQuery):

    # db model
    model: Any = CoreAuthAccounts

    # async def schema(self):

    #     # get schema information
    #     q = await self.schemap()
    #     return q

    async def find_by_email(self, email: str):

        query = select(self.model) \
            .filter(self.model.email == email)
        return await self.find_one(query)

    async def find_user_by_id(self, id: int):

        query = select(self.model) \
            .filter(self.model.id == id)
        return await self.find_one(query)

    async def find_user(self):
        """default paginate search"""

        # filter
        fltr = or_(
            self.model.fullname.ilike(f"%{self.params.q}%"),
            self.model.email.ilike(f"%{self.params.q}%"),
        )

        # ---------------
        # query untuk search
        # .filter(self.model.role == 'admin') \
        # .options(selectinload(self.model.alamat)
        # ---------------

        if self.params.q:
            query = select(self.model) \
                .filter(fltr)
        else:
            query = select(self.model)

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

    async def update_user(self, id: int, data: dict):
        """update user"""
        print("update now", id, data)
        s = await self.update(id, data)
        print(s)
        return {
            "update": True
        }

    # async def create_user(self, data: ReqUserCreate):
    #     """inserting new data"""
    #     await self.insert(data)
    #     return {
    #         "insert": True
    #     }

    # async def get_user(self, id: int):
    #     """Detail by id"""

    #     query = select(self.model) \
    #         .filter(self.model.id == id) \
    #         .options(selectinload(self.model.alamat))

    #     return await self.find_one(query)

    # async def delete_user(self, id: int):
    #     """Delete service"""

    #     await self.delete(id)
    #     return {
    #         "delete": True
    #     }
