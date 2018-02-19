# -*- coding: utf-8 -*-
import random
import string

import pytest as pytest

from model.user import User


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testData = [
    User(name=random_string("name", 10), last_name=random_string("last", 10), nick_name=random_string("nick", 10))
    for i in range(5)
]


@pytest.mark.parametrize("user", testData, ids=[repr(x) for x in testData])
def test_add_new(app, user):
    old_users = app.user_helper.get_user_list()
    app.user_helper.create_and_submit(user)
    app.user_helper.go_to_home_page()
    assert len(old_users) < app.user_helper.count()

    new_users = app.user_helper.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
