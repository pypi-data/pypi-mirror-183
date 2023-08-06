import math
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text, asc, desc, insert, update, delete, Table
from dataclasses import dataclass
from pydantic import PyObject
from sequoia.core.exceptions.base import DuplicateOrSomething
from sequoia.core.schemas import CommonParams
from sequoia.core.db import session
from sequoia.core.config import config


@dataclass
class BaseQuery:
    model: Table
    params: PyObject = CommonParams

    def __sort(self):
        if self.params.order == "asc":
            sort = asc(text(self.params.order_by))
        else:
            sort = desc(text(self.params.order_by))
        return sort

    async def schemap(self):
        tbl = str(self.model.__table__).replace(f"{config.SCHEMA}.", "")
        query = text(
            f"SELECT column_name, data_type \
            FROM information_schema.columns WHERE table_name = '{tbl}';")
        result = await session.execute(query)
        tss = result.mappings().all()
        mydict = {}
        for t in tss:
            mydict[t.column_name] = t.data_type
        return {
            "table": tbl,
            "schema": mydict
        }

    async def count(self, query):

        """
        count rows by query
        """
        result = await session.execute(query)
        count = result.scalar()

        return {
            "total": count,
            "pages": math.ceil(count / self.params.limit),
            "limit": self.params.limit,
            "page": self.params.page,
            "offset": self.params.offset
        }

    async def find(self, query):
        """
        query paginasi
        """

        # add q
        query = query\
            .order_by(self.__sort())\
            .offset(self.params.offset) \
            .limit(self.params.limit)

        result = await session.execute(query)
        return jsonable_encoder(result.scalars().fetchall())

    async def insert(self, data):
        """
        insert data
        """
        try:

            stmt = insert(self.model).values(**data.dict())
            await session.execute(stmt)
            await session.commit()

            return True
        except Exception:
            raise DuplicateOrSomething

    async def update(self, id: int, data: dict):
        """
        update data
        """
        stmt = (
            update(self.model).
            where(self.model.id == id).
            values(data)
        )
        try:
            await session.execute(stmt)
            await session.commit()
        except Exception:
            raise DuplicateOrSomething

    async def find_one(self, query):
        result = await session.execute(query)
        return jsonable_encoder(result.scalars().first())

    async def delete(self, id: int):
        """
        delete data
        """
        stmt = (
            delete(self.model).
            where(self.model.id == id)
        )
        try:
            await session.execute(stmt)
            await session.commit()
        except Exception:
            raise DuplicateOrSomething
