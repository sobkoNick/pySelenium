import random

from model.user import User


def test_del_first_user(app, db):
    if len(db.get_user_list()) == 0:
        app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))

    old_users = db.get_user_list()
    user = random.choice(old_users)

    app.user_helper.delete_user_by_id(user.id)
    app.user_helper.go_to_home_page()

    new_users = db.get_user_list()

    assert len(old_users) == len(new_users)
    old_users.remove(user)
    assert old_users == new_users
