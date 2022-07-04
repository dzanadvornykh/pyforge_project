import logging
from typing import Optional

from .database import DBSession
from .models import Compound


logger = logging.getLogger(__name__)


def get_all_compounds() -> list[Compound]:
    with DBSession() as db:
        compounds = db.query(Compound).all()
        logger.info('compounds received')
    return compounds


def create_compound(compound: Compound) -> None:
    with DBSession() as db:
        db.add(compound)
        db.commit()
        db.refresh(compound)
        logger.info(f"Compound '{compound.compound}' added to db")


def get_compound_by_name(compound_name: str) -> Optional[Compound]:
    with DBSession() as db:
        found = db.query(Compound).filter(Compound.compound == compound_name).first()
        logger.info(f"all compounds with name '{compound_name}' found")
    return found
