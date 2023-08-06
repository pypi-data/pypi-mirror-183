from sqlalchemy import (
    ForeignKey,
    Column,
    BigInteger,
    String,
    Integer,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sequoia.core.config import config
from sequoia.core.db.mixins.timestamp_mixin import TimestampMixin

Base = declarative_base()


class SandboxAccounts(Base, TimestampMixin):
    __tablename__ = "sandbox_accounts"
    __table_args__ = {"schema": config.SCHEMA}

    id = Column(BigInteger, index=True, primary_key=True)
    fullname = Column(String(200), index=True)
    email = Column(String(200), unique=True, index=True)
    status = Column(String(20), index=True)

    alamat = relationship('SandboxAlamat', backref='akun')
    # alamat = relationship("SandboxAlamat", back_populates="account")
    # alamat = relationship("SandboxAlamat")
    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self):
        return f"<SandboxAccounts(fullname='{self.fullname}',\
                                   email='{self.email}') >"


class SandboxAlamat(Base):
    __tablename__ = "sandbox_alamat"
    __table_args__ = {"schema": config.SCHEMA}

    id = Column(BigInteger, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey(
        f"{config.SCHEMA}.sandbox_accounts.id"))
    alamat = Column(String, index=True)
    # akun = relationship('SandboxAccounts', backref='alamat')
    # account = relationship("SandboxAccounts", back_populates="alamat")

    def __repr__(self):
        return "<SandboxAlamat(alamat='{}')>".format(
            self.alamat
        )
