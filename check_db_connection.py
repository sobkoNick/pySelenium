import mysql.connector

from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    list = db.get_contacts_in_group("2")
    for iteam in list:
        print(iteam)
    print(len(list))
finally:
    pass
