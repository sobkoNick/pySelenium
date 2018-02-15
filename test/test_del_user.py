from random import randrange

from model.user import User


def test_del_first_user(app):
    if app.user_helper.count() == 0:
        app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))

    old_users = app.user_helper.get_user_list()
    deleteIndex = randrange(len(old_users))

    app.user_helper.delete_user(deleteIndex)
    app.user_helper.go_to_home_page()

    new_users = app.user_helper.get_user_list()

    assert len(old_users) > len(new_users)
    old_users[deleteIndex:deleteIndex+1] = []
    assert old_users == new_users
