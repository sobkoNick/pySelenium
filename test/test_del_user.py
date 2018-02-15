from model.user import User


def test_del_first_user(app):
    old_users = app.user_helper.get_user_list()
    if app.user_helper.count() == 0:
        app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))
    app.user_helper.delete_first_user()
    app.user_helper.go_to_home_page()
    new_users = app.user_helper.get_user_list()
    old_users[0:1] = []
    assert old_users == new_users
