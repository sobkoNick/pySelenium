from datetime import datetime

from pony.orm import *
from pymysql.converters import decoders

from model.user import User


class ORMFixture:
    db = Database()

    class ORMUser(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstName = Optional(str, column='firstname')
        lastName = Optional(str, column='lastname')
        nickName = Optional(str, column='nickname')
        deprecated = Optional(str, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_user_list(self):
        return self.convert_users_to_model(select(u for u in ORMFixture.ORMUser if u.deprecated is None))

    def convert_users_to_model(self, user):
        def convert(userToConvert):
            return User(id=userToConvert.id, name=userToConvert.firstName, last_name=userToConvert.lastName,
                        nick_name=userToConvert.nickName)
        return list(map(convert, user))
