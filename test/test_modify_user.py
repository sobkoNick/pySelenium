from model.user import User


def test_modify_name(app):
    old_groups = app.user_helper.get_user_list()
    app.user_helper.modify(User(name="Modified name"))
    app.user_helper.back_to_home_page()
    new_groups = app.user_helper.get_user_list()
    assert len(old_groups) == len(new_groups)


def test_modify_last_name(app):
    old_groups = app.user_helper.get_user_list()
    app.user_helper.modify(User(last_name="Modified last name"))
    app.user_helper.back_to_home_page()
    new_groups = app.user_helper.get_user_list()
    assert len(old_groups) == len(new_groups)
