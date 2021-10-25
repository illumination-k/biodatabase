from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from models import Primer

PrimerModel = sqlalchemy_to_pydantic(Primer)