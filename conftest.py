import json

import pytest
from fixture.application import Application
from constants import Constants

fixture = None

target = None

# start fixture with assertion on fixture valid
@pytest.fixture
# @pytest.fixture(scope="session") # use one browser for all tests, BUT IT NEEDS TO ADD LOG OUT TO TEST
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, project_url=target['baseUrl'])

    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


# log-out fixture. runs one time after all test
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def log_out():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(log_out)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
