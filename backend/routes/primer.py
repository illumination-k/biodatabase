from fastapi import APIRouter

from models import db_session
from type_def.reqest_model import CreatePrimerRequest

import query

router = APIRouter(prefix="/primer")

@router.put("/")
def create_primer(req: CreatePrimerRequest):
    session = db_session.session_factory()
    primer = query.create_primer(session=session, req=req)