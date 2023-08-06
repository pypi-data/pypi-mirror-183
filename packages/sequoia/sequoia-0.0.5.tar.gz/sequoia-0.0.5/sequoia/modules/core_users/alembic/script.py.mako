"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
import os
import ujson
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from modules.core_users.models import CoreUsersAccounts
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

__table__ = "core_users_accounts"


def createTable():
    bind = op.get_bind()
    CoreUsersAccounts.__table__.create(bind)
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
        # ec.append(
        #     CoreUsersAccounts(
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
    op.drop_table(
        __table__,
        schema=op.get_context().dialect.schema,
    )
    pass
