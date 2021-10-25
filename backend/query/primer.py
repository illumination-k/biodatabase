from typing import Optional, Type
from sqlalchemy.orm.session import Session

from type_def.reqest_model import CreatePrimerRequest
from models import Primer
from utils.primer import calc_gc, calc_tm


def create_primer(*, session: Session, req: CreatePrimerRequest) -> Optional[Primer]:
    tm = calc_tm(req.seq)
    gc = calc_gc(req.seq)

    primer_dict = req.dict()
    primer_dict["tm"] = tm
    primer_dict["gc"] = gc
    primer = Primer(**primer_dict)

    try:
        session.add(primer)
        session.commit()
    except:
        session.rollback()

    