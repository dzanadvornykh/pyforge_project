import pytest
from apps.validation import InvalidCompoundError, CompoundAlreadyInDBError
from apps.getting_info import get_info_about_compound


def test_valid_name(compound_mock, api_mock):
    compound_mock.return_value = None
    name = 'ATP'
    get_info_about_compound(name)


def test_invalid_name(compound_mock):
    compound_mock.return_value = None
    name = 'Aspirin'
    with pytest.raises(InvalidCompoundError):
        get_info_about_compound(name)


def test_already_in_db(compound_mock):
    compound_mock.return_value = True
    name = 'ATP'
    with pytest.raises(CompoundAlreadyInDBError):
        get_info_about_compound(name)
