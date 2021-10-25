from sqlalchemy import Column
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import ARRAY, Float, Integer, String, TEXT

from .utils import create_engine

Engine = create_engine()

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=Engine)
)

Base = declarative_base()

# declare for query
Base.query = db_session.query_property()


class Primer(Base):
    __tablename__ = "primer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    seq = Column(String)
    gc = Column(Float)
    tm = Column(Float)
    aliases = Column(ARRAY(String), nullable=True)
    note = Column(String, nullable=True)
    description = Column(TEXT, nullable=True)
