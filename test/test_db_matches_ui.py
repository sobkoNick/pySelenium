from model.user import User


def test_user_list(app, db):
    def clean(user):
        return User(id=user.id, name=user.name.strip())
    ui_list = app.user_helper.get_user_list()
    db_list = map(clean, db.get_user_list())
    # assert len(ui_list) == len(db_list)
    assert sorted(ui_list, key=User.id_or_max) == sorted(db_list, key=User.id_or_max)