import os
import toml
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool, text
from alembic import context
from munch import DefaultMunch


def load_toml():
    s = context.get_x_argument(as_dictionary=True)
    if s.get("stage"):
        stage = s.get("stage")
    else:
        stage = "local"

    print("Running as: ", stage)
    os.environ["PROJECT_STAGE"] = stage

    t = toml.load(os.path.join(f"../../../.env.{stage}.toml"))
    if "SCHEMA" in t:
        schema = t["SCHEMA"]
    else:
        schema = os.getenv("SCHEMA") or "z_local"
    t["SCHEMA"] = schema
    os.environ["SCHEMA"] = schema

    tt = DefaultMunch.fromDict(t, object())
    return tt


cfg = load_toml()


def get_schema():
    s = context.get_x_argument(as_dictionary=True)
    if s.get("schema"):
        scm = s.get("schema")
        os.environ["SCHEMA"] = scm
    else:
        scm = os.getenv("SCHEMA")
    return scm


pathdir = os.path.abspath(".")
vertable = "alembic_" + os.path.basename(pathdir).strip()
schema = get_schema()

print("schema", schema)
config = context.config
config.set_main_option(
    "sqlalchemy.url", cfg.DB.POSTGRE.MAIN.WRITE.replace("asyncpg", "psycopg2")
)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        # create schema
        connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
        connection.execute(text(f"set search_path to {schema}"))
        connection.commit()

        connection.dialect.schema = schema

        context.configure(
            connection=connection,
            version_table=vertable,
            target_metadata=None,
            include_schemas=True,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
