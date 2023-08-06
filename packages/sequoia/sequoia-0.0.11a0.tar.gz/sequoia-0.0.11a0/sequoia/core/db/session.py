import os
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_scoped_session,
)
from typing import Union
from contextvars import ContextVar, Token
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql.expression import Update, Delete, Insert
from sequoia.core.config import config

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


# type: ignore
nt = True
if os.getenv("PROJECT_STAGE") == 'prod':
    nt = False

engines = {
    "writer": create_async_engine(
        config.DB.POSTGRE.MAIN.WRITE,  # type: ignore
        pool_recycle=3600,
        echo=nt
    ),
    "reader": create_async_engine(
        config.DB.POSTGRE.MAIN.READ,  # type: ignore
        pool_recycle=3600,
        echo=nt
    ),
}


class RoutingSession(Session):
    def get_bind(self, mapper=None, clause=None, **kw):
        if self._flushing or isinstance(clause, (Update, Delete, Insert)):
            return engines["writer"].sync_engine
        else:
            return engines["reader"].sync_engine


engine = create_engine(
    config.DB.POSTGRE.MAIN.WRITE.replace(  # type: ignore
        "asyncpg", "psycopg2"),
    pool_size=400,
    max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)


async_session_factory = sessionmaker(
    class_=AsyncSession,
    sync_session_class=RoutingSession,
)
session: Union[AsyncSession, async_scoped_session] = async_scoped_session(
    session_factory=async_session_factory,  # type: ignore
    scopefunc=get_session_context,
)
Base = declarative_base()
