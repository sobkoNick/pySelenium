import mysql.connector

from model.user import User


class DbFixture:
    def __init__(self, host, name, user, password) -> None:
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_user_list(self):
        userList = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, nickname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstName, lastName, nickName) = row
                userList.append(User(id=id, name=firstName, last_name=lastName, nick_name=nickName))
        finally:
            cursor.close()
        return userList

    def destroy(self):
        self.connection.close()
