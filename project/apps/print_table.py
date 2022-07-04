import prettytable

from .models import Compound
from .crud import get_all_compounds


def get_table() -> prettytable.PrettyTable:
    table = prettytable.PrettyTable(field_names=Compound.colnames())

    for compound in get_all_compounds():
        table.add_row(compound.values)

    return table
