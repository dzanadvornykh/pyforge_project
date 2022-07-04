import pytest

from .data import ATP_INFO


@pytest.fixture(scope='function')
def compound_mock(mocker):
    return mocker.patch(
        "apps.validation.get_compound_by_name"
    )


@pytest.fixture(scope='function')
def api_mock(mocker):
    return mocker.patch(
        "apps.getting_info.get_info_from_api",
        return_value=ATP_INFO,
    )