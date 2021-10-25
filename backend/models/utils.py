import os
import sqlalchemy
from sqlalchemy.engine.base import Engine


def get_postgres_url():
    url = os.environ.get("DATABASE_URI")
    if url is not None:
        return url

    if os.path.exists("/.dockerenv"):
        return "postgresql://postgres:postgres@postgres:5432/main"

    return "postgresql://postgres:postgres@localhost:5432/main"


def create_engine() -> Engine:
    if os.environ.get("DEBUG") is not None:
        echo = True
    else:
        echo = False
    return sqlalchemy.create_engine(get_postgres_url(), encoding="utf-8", echo=echo)


# model to dict
def to_dict(model) -> dict:
    return dict((col.name, getattr(model, col.name)) for col in model.__table__.columns)