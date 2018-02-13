# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_seconf(app):
    app.login(username="admin", password="secret")
    app.crate_and_submit(User(name="asdasd", last_name="dfsfds", nick_name="asdfsd"))
    app.home_page()


def test_second_empty(app):
    app.login(username="admin", password="secret")
    app.crate_and_submit(User(name="name", last_name="last", nick_name="nick"))
    app.home_page()
