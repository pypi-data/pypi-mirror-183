"""create core_users_alamat

Revision ID: 2e5d0663fdbe
Revises: 321b4239aad9
Create Date: 2022-12-22 14:52:31.055508

"""
import os
import ujson
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from modules.core_auth.models import CoreAuthAlamat


# revision identifiers, used by Alembic.
revision = '2e5d0663fdbe'
down_revision = '321b4239aad9'
branch_labels = None
depends_on = None

__table__ = CoreAuthAlamat.__tablename__


def createTable():
    bind = op.get_bind()
    CoreAuthAlamat.__table__.create(bind)
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
            CoreAuthAlamat(
                account_id=data["account_id"],
                alamat=data["alamat"],
            )
        )
    session.add_all(ec)
    session.commit()


def upgrade() -> None:
    # createTableOp()
    createTable()
    faktory()


def downgrade() -> None:
    op.drop_table(
        __table__,
        schema=op.get_context().dialect.schema,
    )
    pass
