"""create insert data

Revision ID: f1a23abb7b28
Revises: 1f307f913d1b
Create Date: 2022-12-05 00:53:37.884547

"""
import os
import ujson
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from modules.core_sandbox.models import SandboxAccounts, SandboxAlamat


# revision identifiers, used by Alembic.
revision = 'f1a23abb7b28'
down_revision = '1f307f913d1b'
branch_labels = None
depends_on = None

__table__ = "sandbox_accounts"


def createTable():
    bind = op.get_bind()
    # SandboxAccounts.__table__.create(bind)
    pass


def createTableOp():
    schema = op.get_context().dialect.schema
    op.create_table(
        __table__,
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("fullname", sa.String(200), nullable=False),
        sa.Column("email", sa.String(200), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        # sa.ForeignKeyConstraint(
        #     ("warehouse_id",),
        #     ["core_stock_warehouse.id"],
        # ),
        schema=schema,
    )


def faktory():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    pj = os.path.join(
        os.path.dirname(os.path.abspath(__file__)
                        ), "../data", f"{__table__}.json"
    )
    f = open(pj)
    datas = ujson.load(f)
    ec = []
    for data in datas:
        print("Insert data", data)
        ec.append(
            SandboxAccounts(
                email=data["email"], fullname=data["fullname"], status=data["status"]
            )
        )
    session.add_all(ec)
    session.commit()


def faktoryAlamat():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    pj = os.path.join(
        os.path.dirname(os.path.abspath(__file__)
                        ), "../data", "sandbox_alamat.json"
    )
    f = open(pj)
    datas = ujson.load(f)
    ec = []
    for data in datas:
        print("Insert data", data)
        ec.append(
            SandboxAlamat(
                alamat=data["alamat"], account_id=data["account_id"]
            )
        )
    session.add_all(ec)
    session.commit()


def upgrade() -> None:
    # createTableOp()
    # createTable()
    faktory()
    faktoryAlamat()


def downgrade() -> None:
    # op.drop_table(
    #     __table__,
    #     schema=op.get_context().dialect.schema,
    # )
    pass
