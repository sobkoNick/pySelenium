

def test_del_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user_helper.delete_first_user()
