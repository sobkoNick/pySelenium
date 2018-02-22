import importlib
import json

import os

import jsonpickle
import pytest
from fixture.application import Application
from constants import Constants
from fixture.db import DbFixture

fixture = None
target = None

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as file:
            target = json.load(file)
    return target

# start fixture with assertion on fixture valid
@pytest.fixture
# @pytest.fixture(scope="session") # use one browser for all tests, BUT IT NEEDS TO ADD LOG OUT TO TEST
def app(request):
    global fixture

    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, project_url=web_config['baseUrl'])

    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbFixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])
    def fin():
        dbFixture.destroy()
    request.addfinalizer(fin)
    return dbFixture


# log-out fixture. runs one time after all test
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def log_out():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(log_out)
    return fixture

@pytest.fixture()
def check_ui(request):
    return request.config.getoption("--check_ui")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):  # add dynamic data binding from file data/users.py
    for fixt in metafunc.fixturenames:
        if fixt.startswith("data_"):  # if test has parameter like 'data_' (data_users)
            testData = load_from_module(fixt[5:])  # upload data from module that is '#data_#USERS'
            metafunc.parametrize(fixt, testData, ids=[str(x) for x in testData])  # (app, data_users)
        elif fixt.startswith("json_"):
            testData = load_from_json(fixt[5:])
            metafunc.parametrize(fixt, testData, ids=[str(x) for x in testData])  # (app, json_users)

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testData


def load_from_json(file):
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)
    with open(json_file) as jfile:
        return jsonpickle.decode(jfile.read())