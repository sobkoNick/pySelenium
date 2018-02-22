from timeit import timeit

from model.user import User


def test_user_list(app, db):
    def clean(user):
        return User(id=user.id, name=user.name.strip())
    ui_list = app.user_helper.get_user_list()
    db_list = map(clean, db.get_user_list())

    print(timeit(lambda: app.user_helper.get_user_list(), number=1))
    print(timeit(lambda: db.get_user_list(), number=100))

    # assert len(ui_list) == len(db_list)
    assert sorted(ui_list, key=User.id_or_max) == sorted(db_list, key=User.id_or_max)