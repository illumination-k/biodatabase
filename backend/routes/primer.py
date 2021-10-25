from typing import List, Optional
from fastapi import APIRouter, HTTPException

from models import db_session
from type_def.reqest_model import CreatePrimerRequest
from type_def.orm import PrimerModel

import query

router = APIRouter(prefix="/primer")


@router.post("/", response_model=PrimerModel)
def create_primer(req: CreatePrimerRequest):
    session = db_session.session_factory()
    primer = query.create_primer(session=session, req=req)
    if primer is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return PrimerModel.from_orm(primer)


@router.get("/all", response_model=List[PrimerModel])
def get_all_primers():
    session = db_session.session_factory()
    primers = query.get_all_primers(session=session)
    return primers


@router.get("/search", response_model=List[PrimerModel])
def search_primers(words: Optional[str] = None):
    session = db_session.session_factory()
    return query.search_primers(session=session, words=words)
