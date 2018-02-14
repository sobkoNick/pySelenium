import pytest
from fixture.application import Application
from constants import Constants

fixture = None

# start fixture with assertion on fixture valid
@pytest.fixture
# @pytest.fixture(scope="session") # use one browser for all tests, BUT IT NEEDS TO ADD LOG OUT TO TEST
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username=Constants.USER_NAME, password=Constants.PASSWORD)
    return fixture


# log-out fixture. runs one time after all test
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def log_out():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(log_out)
    return fixture
