from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import (
    ARRAY,
    Float,
    Integer,
    String,
    TEXT,
    LargeBinary,
    DateTime,
    Boolean,
)

from .utils import create_engine

Engine = create_engine()

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=Engine)
)

Base = declarative_base()

# declare for query
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True)

    # default informations
    username = Column(String)
    email = Column(String)
    password = Column(TEXT)
    first_name = Column(String)
    last_name = Column(String)

    # optional information
    picture = Column(LargeBinary, nullable=True)

    # permission
    active = Column(Boolean)

    # log
    registered = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now())

    # child relations
    primer = relationship("Primer")


class Primer(Base):
    __tablename__ = "primer"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    seq = Column(String)
    gc = Column(Float)
    tm = Column(Float)
    aliases = Column(ARRAY(String), nullable=True)
    note = Column(String, nullable=True)
    description = Column(TEXT, nullable=True)
    registered = Column(DateTime, default=func.now())
    updated = Column(DateTime, default=func.now())

    user_id = Column(Integer, ForeignKey("user.id"))
