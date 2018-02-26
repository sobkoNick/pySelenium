from datetime import datetime

from pony.orm import *
from pymysql.converters import decoders

from model.user import User


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMUser, table='address_in_groups', column='id', reverse="groups", lazy=True)

    class ORMUser(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstName = Optional(str, column='firstname')
        lastName = Optional(str, column='lastname')
        nickName = Optional(str, column='nickname')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse="contacts",
                     lazy=True)

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

    @db_session
    def get_contacts_in_group(self, groupId):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == groupId))[0]
        return self.convert_users_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, groupId):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == groupId))[0]
        return self.convert_users_to_model(
            select(u for u in ORMFixture.ORMUser if u.deprecated is None and orm_group not in u.groups))
