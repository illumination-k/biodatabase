from typing import List, Optional
from pydantic import BaseModel


class CreatePrimerRequest(BaseModel):
    name: str
    seq: str
    aliases: Optional[List[str]]
    note: Optional[str]
    description: Optional[str]
