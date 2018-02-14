from model.user import User


def test_modify_name(app):
    app.user_helper.modify(User(name="Modified name"))


def test_modify_last_name(app):
    app.user_helper.modify(User(last_name="Modified last name"))
