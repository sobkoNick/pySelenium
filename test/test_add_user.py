# -*- coding: utf-8 -*-
import time


from model.user import User


def test_add_new(app):
    old_users = app.user_helper.get_user_list()
    user = User(name="My name", last_name="My last name", nick_name="My nick name")
    app.user_helper.create_and_submit(user)
    app.user_helper.go_to_home_page()
    assert len(old_users) < app.user_helper.count()

    time.sleep(3)
    new_users = app.user_helper.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
    # app.session.logout() # test if fixture works well when you log out


# def test_add_empty(app):
#     old_users = app.user_helper.get_user_list()
#     user = User(name="My name", last_name="", nick_name="My nick name")
#     app.user_helper.create_and_submit(user)
#     app.user_helper.go_to_home_page()
#     time.sleep(3)
#     new_users = app.user_helper.get_user_list()
#     assert len(old_users) < len(new_users)
#     old_users.append(user)
#     assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
