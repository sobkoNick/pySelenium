from model.user import User
from random import randrange


def test_modify_name(app):
    if app.user_helper.count() == 0:
        app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))
    old_users = app.user_helper.get_user_list()

    modifyIndex = randrange(len(old_users))
    user = User(name="Modified name")
    user.id = old_users[modifyIndex].id

    app.user_helper.modify(user, modifyIndex)
    app.user_helper.go_to_home_page()

    new_users = app.user_helper.get_user_list()

    assert len(old_users) == len(new_users)
    old_users[modifyIndex] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)


# def test_modify_last_name(app):
#     old_users = app.user_helper.get_user_list()
#     app.user_helper.modify(User(last_name="Modified last name"))
#     app.user_helper.go_to_home_page()
#     new_users = app.user_helper.get_user_list()
#     assert len(old_users) == len(new_users)
