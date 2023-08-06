from sqlalchemy import (
    ForeignKey,
    Column,
    BigInteger,
    String,
    Integer,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from core.config import config
from sequoia.core.db.mixins.timestamp_mixin import TimestampMixin

Base = declarative_base()
schema = 'public'  # config.SCHEMA


class CoreUsersAccounts(Base, TimestampMixin):
    __tablename__ = "core_users_accounts"
    __table_args__ = {"schema": schema}

    id = Column(BigInteger, index=True, primary_key=True)
    fullname = Column(String(200), index=True)
    email = Column(String(200), unique=True, index=True)
    role = Column(String(200), index=True, default="user")
    status = Column(String(20), index=True, default="inactive")

    alamat = relationship('CoreUsersAlamat', backref='akun')

    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self):
        return f"<CoreUsersAccounts(fullname='{self.fullname}',\
                                   email='{self.email}') >"


class CoreUsersAlamat(Base):
    __tablename__ = "core_users_alamat"
    __table_args__ = {"schema": schema}

    id = Column(BigInteger, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey(
        f"{schema}.core_users_accounts.id"))
    alamat = Column(String, index=True)
    # akun = relationship('CoreUsersAccounts', backref='alamat')

    def __repr__(self):
        return f"<CoreUsersAlamat(\
            account_id='{self.account_id}' \
            alamat='{self.alamat}')>"
