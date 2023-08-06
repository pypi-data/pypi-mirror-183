"""create main_tasks

Revision ID: f99690d24508
Revises: 
Create Date: 2022-12-15 09:07:07.241194

"""
import os
import ujson
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from modules.core_main.models import MainTasks


# revision identifiers, used by Alembic.
revision = 'f99690d24508'
down_revision = None
branch_labels = None
depends_on = None

__table__ = "core_main_tasks"
schema = "public"


def createTable():
    bind = op.get_bind()
    MainTasks.__table__.create(bind)
    pass


def createTableOp():
    # schema = op.get_context().dialect.schema
    op.create_table(
        __table__,

        sa.Column("module", sa.String(200), nullable=False),
        sa.Column("taskname", sa.String(200), nullable=False),
        sa.Column("msg", sa.String, nullable=True),
        sa.Column("user_id", sa.BigInteger, nullable=True, default=1),
        sa.Column("link", sa.String, nullable=True),
        sa.Column("meta", sa.JSON, nullable=True),
        sa.Column("conclusion", sa.String(20),
                  nullable=False, default="queue"),
        sa.Column("status", sa.String(20),
                  nullable=False, default="created"),

        sa.ForeignKeyConstraint(
            ("user_id",),
            ["core_users_accounts.id"],
        ),
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
        # ec.append(
        #     CoreMainAccounts(
        #         email=data["email"], fullname=data["fullname"], status=data["status"]
        #     )
        # )
    session.add_all(ec)
    session.commit()


def upgrade() -> None:
    # createTableOp()
    createTable()
    # faktory()


def downgrade() -> None:
    # op.get_context().dialect.schema
    op.drop_table(
        __table__,
        schema=schema,
    )
    pass
