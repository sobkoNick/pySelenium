# -*- coding: utf-8 -*-

from model.user import User


def test_add_new(app):
    app.user_helper.create_and_submit(User(name="My name", last_name="My last name", nick_name="My nick name"))
    app.user_helper.back_to_home_page()
    # app.session.logout() # test if fixture works well when you log out


def test_add_empty(app):
    app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))
    app.user_helper.back_to_home_page()
