import pytest
from fixture.application import Application
import json
import os.path
from fixture.db import DbFixture

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config=load_config(request.config.getoption("--target"))['web']
    soap_config = load_config(request.config.getoption("--target"))['soap']
    fixture = Application(browser=browser, base_url = web_config['baseUrl'], soap_url = soap_config['soap_url'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture(scope="session")
def db(request):
    dbfixture = DbFixture(host='localhost', database='bugtracker', user='root', password='')
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


