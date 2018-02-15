from sys import maxsize

class User:
    def __init__(self, name=None, last_name=None, nick_name=None, id=None):
        self.name = name
        self.last_name = last_name
        self.nick_name = nick_name
        self.id = id

    def __repr__(self) -> str:
        return "User(%s, %s, %s, %s)" % (self.name, self.last_name, self.nick_name, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

