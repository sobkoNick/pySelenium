# -*- coding: utf-8 -*-

from model.user import User


def test_add_new(app):
    old_groups = app.user_helper.get_user_list()
    app.user_helper.create_and_submit(User(name="My name", last_name="My last name", nick_name="My nick name"))
    app.user_helper.back_to_home_page()
    new_groups = app.user_helper.get_user_list()
    assert len(old_groups) < len(new_groups)
    # app.session.logout() # test if fixture works well when you log out


def test_add_empty(app):
    old_groups = app.user_helper.get_user_list()
    app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))
    app.user_helper.back_to_home_page()
    new_groups = app.user_helper.get_user_list()
    assert len(old_groups) < len(new_groups)
