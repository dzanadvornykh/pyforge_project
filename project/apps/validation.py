from .crud import get_compound_by_name


COMPOUNDS = (
    'ADP',
    'ATP',
    'STI',
    'ZID',
    'DPM',
    'XP9',
    '18W',
    '29P',
)


class InvalidCompoundError(ValueError):
    def __init__(self, compound, *args: object) -> None:
        self.detail = f"Invalid compound '{compound}'"
        super().__init__(*args)

class CompoundAlreadyInDBError(ValueError):
    def __init__(self, compound, *args: object) -> None:
        self.detail = f"Compound '{compound}' already in DB"
        super().__init__(*args)


def validate_compound(compound: str) -> None:
    if compound not in COMPOUNDS:
        raise InvalidCompoundError(compound)


def validate_compound_existence(compound: str) -> None:
    if get_compound_by_name(compound):
        raise CompoundAlreadyInDBError(compound)
