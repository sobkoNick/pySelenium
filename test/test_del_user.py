from model.user import User


def test_del_first_user(app):
    if app.user_helper.count() == 0:
        app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))
    app.user_helper.delete_first_user()
