from model.user import User


def test_modify_name(app):
    old_users = app.user_helper.get_user_list()
    user = User(name="Modified name")
    user.id = old_users[0].id
    app.user_helper.modify(user)
    app.user_helper.go_to_home_page()
    new_users = app.user_helper.get_user_list()
    assert len(old_users) == len(new_users)
    old_users[0] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)


# def test_modify_last_name(app):
#     old_users = app.user_helper.get_user_list()
#     app.user_helper.modify(User(last_name="Modified last name"))
#     app.user_helper.go_to_home_page()
#     new_users = app.user_helper.get_user_list()
#     assert len(old_users) == len(new_users)
