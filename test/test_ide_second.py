# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_second(app):
    app.session.login(username="admin", password="secret")
    app.add_new.crate_and_submit(User(name="My name", last_name="My last name", nick_name="My nick name"))
    app.add_new.back_to_home_page()


def test_second_empty(app):
    app.session.login(username="admin", password="secret")
    app.add_new.crate_and_submit(User(name="name", last_name="last", nick_name="nick"))
    app.add_new.back_to_home_page()
