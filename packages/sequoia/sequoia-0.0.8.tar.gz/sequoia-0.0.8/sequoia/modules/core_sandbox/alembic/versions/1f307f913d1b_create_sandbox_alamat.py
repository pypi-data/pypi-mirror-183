"""create sandbox_alamat

Revision ID: 1f307f913d1b
Revises: 32bf36670584
Create Date: 2022-12-05 00:48:10.112086

"""
from alembic import op
import sqlalchemy as sa
from modules.core_sandbox.models import SandboxAccounts, SandboxAlamat


# revision identifiers, used by Alembic.
revision = '1f307f913d1b'
down_revision = '32bf36670584'
branch_labels = None
depends_on = None

__table__ = "sandbox_alamat"


def createTable():
    bind = op.get_bind()
    SandboxAlamat.__table__.create(bind)
    pass


def createTableOp():
    schema = op.get_context().dialect.schema

    op.create_table(
        __table__,
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("account_id", sa.Integer),
        sa.Column("alamat", sa.String, nullable=False),
        sa.ForeignKeyConstraint(
            ("account_id",),
            ["sandbox_accounts.id"],
        ),
        schema=schema,
    )
    pass


def upgrade() -> None:
    createTable()
    # createTableOp()

    # pj = os.path.join(
    #     os.path.dirname(os.path.abspath(__file__)), "../data", "users.json"
    # )
    # f = open(pj)
    # datas = ujson.load(f)
    # ec = []
    # for data in datas:
    #     print("Insert data", data)
    #     ec.append(
    #         SandboxAccounts(
    #             email=data["email"], fullname=data["fullname"], status=data["status"]
    #         )
    #     )

    # session.add_all(ec)
    # session.commit()


def downgrade() -> None:
    op.drop_table(
        __table__,
        schema=op.get_context().dialect.schema,
    )
    pass
