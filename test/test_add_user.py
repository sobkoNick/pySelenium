# -*- coding: utf-8 -*-


# from data.add_user import testData
from model.user import User


def test_add_new(app, db, json_users):
    user = json_users
    old_users = db.get_user_list()
    app.user_helper.create_and_submit(user)
    app.user_helper.go_to_home_page()

    # assert len(old_users) < app.user_helper.count()

    new_users = db.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
