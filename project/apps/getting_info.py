import logging
import requests

from .crud import create_compound
from .models import Compound
from .validation import CompoundAlreadyInDBError, InvalidCompoundError, validate_compound, validate_compound_existence


logger = logging.getLogger(__name__)

API_URL = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/{compound}'


def parse_json(compound: str, data: dict) -> Compound:
    
    data_ = data[compound][0]
    return Compound(
        compound=compound,
        name=data_['name'],
        formula = data_['formula'],
        inchi = data_['inchi'],
        inchi_key = data_['inchi_key'],
        smiles = data_['smiles'],
        cross_links_count = len(data_['cross_links']),
    )


def get_info_from_api(compound: str) -> dict:
    response = requests.get(
        url=API_URL.format(compound=compound),
        timeout=1,
    )
    return response.json()


def get_info_about_compound(compound: str) -> Compound:
    validate_compound(compound)
    validate_compound_existence(compound)
    logger.info(f"Compound '{compound}' valid")
    res = get_info_from_api(compound)
    logger.info(f'Information from api received')

    return parse_json(compound, res)


def send_info_to_db(compound_alias: str) -> None:
    try:
        logger.info(f"Start working with compound '{compound_alias}'")
        compound = get_info_about_compound(compound_alias)
    except (CompoundAlreadyInDBError, InvalidCompoundError) as e:
        logger.error(e.detail)
        print(f"Error: {e.detail}")
    else:
        create_compound(compound)
        print(f"Compound {compound_alias} succesfully added to db")
