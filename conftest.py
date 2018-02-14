import pytest
from fixture.application import Application


# @pytest.fixture
@pytest.fixture(scope="session") # use one browser for all tests, BUT IT NEEDS TO ADD LOG OUT TO TEST
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
