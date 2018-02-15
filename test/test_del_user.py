from model.user import User


def test_del_first_user(app):
    old_groups = app.user_helper.get_user_list()
    if app.user_helper.count() == 0:
        app.user_helper.create_and_submit(User(name="name", last_name="last", nick_name="nick"))
    app.user_helper.delete_first_user()
    app.user_helper.back_to_home_page()
    new_groups = app.user_helper.get_user_list()
    assert len(old_groups) > len(new_groups)
