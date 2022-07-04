from typing import Union

from sqlalchemy import Column, Integer, String

from .database import Base


MAX_FIELD_LEN = 13
FIELD_LEN = 10


class Compound(Base):
    __tablename__ = "compound"

    compound = Column(String, primary_key=True, index=True)
    name = Column(String)
    formula = Column(String)
    inchi = Column(String)
    inchi_key = Column(String)
    smiles = Column(String)
    cross_links_count = Column(Integer)

    @classmethod
    def colnames(cls) -> list[str]:
        return [column.name for column in cls.__table__.columns]

    def _get_value(self, name: str) -> Union[str, int]:
        value = getattr(self, name)
        if isinstance(value, str) and len(value) >= MAX_FIELD_LEN:
            return f"{value[:FIELD_LEN]}..."
        return value

    @property
    def values(self) -> list:
        return [self._get_value(name) for name in self.colnames()]

    def __repr__(self) -> str:
        return f"compound: {self.compound},\n name: {self.name},\n formula: {self.formula}"
