from sqlalchemy import (
    Column,
    BigInteger,
    String,
    ForeignKey,
    JSON,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from core.config import config
from modules.core_auth.models import CoreAuthAccounts
from core.db.mixins.timestamp_mixin import TimestampMixin

Base = declarative_base()
schema = "public"  # config.SCHEMA


class MainConfig(Base):
    __tablename__ = "core_main_config"
    __table_args__ = {"schema": schema}

    id = Column(BigInteger, primary_key=True, index=True)
    key = Column(String(200), index=True)
    value = Column(String, index=True)

    def __repr__(self):
        return "<MainConfig(key='{}', value='{}')>".format(
            self.key, self.value
        )


class MainTasks(Base, TimestampMixin):
    """Default task logs"""
    __tablename__ = "core_main_tasks"
    __table_args__ = {"schema": schema}

    id = Column(String, primary_key=True, index=True)
    module = Column(String(200), index=True)
    taskname = Column(String(200), index=True)

    # account_id = Column(BigInteger, ForeignKey(
    #     f"{schema}.core_users.id"))

    msg = Column(String)
    link = Column(String)
    meta = Column(JSON)
    conclusion = Column(String(200), index=True, default="queue")
    status = Column(String(200), index=True, default="created")
    user_id = Column(BigInteger, ForeignKey(
        "public.core_users.id"))
    # user_id = relationship('CoreAuthAccounts')

    def __repr__(self):
        return f"<MainTasks(module='{self.module}', \
            taskname='{self.taskname}', conclusion='{self.conclusion}')>"


class MainTimezone(Base):
    __tablename__ = "core_main_timezone"
    __table_args__ = {"schema": schema}

    id = Column(BigInteger, primary_key=True, index=True)
    label = Column(String(200), index=True)
    tz_code = Column(String(200), index=True)
    name = Column(String(200), index=True)
    utc = Column(String(200), index=True)


class XUsers(Base):
    __tablename__ = "core_users"
    __table_args__ = {"extend_existing": True, "schema": schema}
    id = Column(BigInteger, primary_key=True, index=True)
