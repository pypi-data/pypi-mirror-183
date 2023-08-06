"""create main_timezone

Revision ID: 239982f68686
Revises: f99690d24508
Create Date: 2022-12-18 09:19:16.714629

"""
import os
import ujson
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from modules.core_main.models import MainTimezone


# revision identifiers, used by Alembic.
revision = '239982f68686'
down_revision = 'f99690d24508'
branch_labels = None
depends_on = None

__table__ = "core_main_timezone"
schema = "public"


def createTable():
    bind = op.get_bind()
    MainTimezone.__table__.create(bind)
    pass


def createTableOp():
    # schema = op.get_context().dialect.schema
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
            MainTimezone(
                label=data["label"],
                tz_code=data["tz_code"],
                name=data["utc"],
                utc=data["utc"]
            )
        )
    session.add_all(ec)
    session.commit()


def upgrade() -> None:
    # createTableOp()
    createTable()
    faktory()


def downgrade() -> None:
    # op.get_context().dialect.schema
    op.drop_table(
        __table__,
        schema=schema,
    )
    pass
