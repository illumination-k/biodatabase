from typing import Optional, List
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.elements import or_

from type_def.reqest_model import CreatePrimerRequest
from models import Primer
from type_def.orm import PrimerModel
from utils.primer import calc_gc, calc_tm, kmerlize


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

        return primer
    except:
        session.rollback()
        return None


def get_all_primers(*, session: Session) -> List[PrimerModel]:
    return [PrimerModel.from_orm(q) for q in session.query(Primer).all()]


def search_primers(*, session: Session, words: Optional[str]):
    queries = session.query(Primer)
    if words is not None:
        for word in words.split(" "):
            queries = queries.filter(
                or_(
                    Primer.name.contains(word),
                    Primer.aliases.contains(word),
                    Primer.note.contains(word),
                    Primer.description.contains(word),
                )
            )

    return [PrimerModel.from_orm(q) for q in queries.all()]


def get_primer_by_seq(db: Session, seq: str) -> Optional[Primer]:
    seqs = kmerlize(seq, k=15)
    q = db.query(Primer)
    
    for seq in seqs:
        q.filter(getattr(Primer, "seq").contains(seq))
        
    return q.all()
