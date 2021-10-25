from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from models import Primer

_PrimerModel = sqlalchemy_to_pydantic(Primer)


class PrimerModel(_PrimerModel):
    class Config:
        orm_mode: True
