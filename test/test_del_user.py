import random

from model.user import User


def test_del_first_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))

    oldUsers = db.get_user_list()
    user = random.choice(oldUsers)

    app.user_helper.delete_user_by_id(user.id)
    app.user_helper.go_to_home_page()

    newUsers = db.get_user_list()
    oldUsers.remove(user)
    assert len(oldUsers) == len(newUsers)
    assert oldUsers == newUsers
    if check_ui:
        print("check ui works")
        assert sorted(newUsers, key=User.id_or_max)  == sorted(app.user_helper.get_user_list(), key=User.id_or_max)
