from sqlalchemy import (
    ForeignKey,
    Column,
    BigInteger,
    String,
    Integer,
    DateTime,
    Boolean
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from sequoia.core.config import config
from sequoia.core.db.mixins.timestamp_mixin import TimestampMixin

Base = declarative_base()
schema = "public"  # config.SCHEMA


class CoreAuthAccounts(Base, TimestampMixin):
    __tablename__ = "core_users"
    __table_args__ = {"schema": schema}

    id = Column(BigInteger, primary_key=True, index=True)
    fullname = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    username = Column(String(100), index=True)
    whatsapp = Column(String(20), unique=True, index=True)
    password = Column(String)
    lastlogin = Column(DateTime, default=None)
    role = Column(String(15), index=True)
    meta_resetkey = Column(String(100))
    avatar = Column(String, nullable=True, default="")
    is_verified = Column(Boolean, default=False)
    status = Column(String(10), default="inactive")
    regcode = Column(String(100), default="")

    # alamat = relationship('CoreAuthAlamat', backref='akun')
    # alamat = relationship("CoreAuthAlamat", back_populates="account")
    # alamat = relationship("CoreAuthAlamat")
    __mapper_args__ = {"eager_defaults": True}

    # def __repr__(self):
    #     return f"<CoreAuthAccounts(fullname='{self.fullname}',\
    #                                email='{self.email}') >"


class CoreAuthAlamat(Base):
    __tablename__ = "core_users_alamat"
    __table_args__ = {"schema": schema}

    id = Column(BigInteger, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey(
        f"{schema}.core_users.id"))
    alamat = Column(String, index=True)
    # akun = relationship('CoreAuthAccounts', backref='alamat')
    # account = relationship("CoreAuthAccounts", back_populates="alamat")

    def __repr__(self):
        return "<CoreAuthAlamat(alamat='{}')>".format(
            self.alamat
        )
