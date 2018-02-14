from model.user import User


def test_modify_name(app):
    app.session.login(username="admin", password="secret")
    app.user_helper.modify(User(name="Modified name"))
    app.session.logout()


def test_modify_last_name(app):
    app.session.login(username="admin", password="secret")
    app.user_helper.modify(User(last_name="Modified last name"))
    app.session.logout()
