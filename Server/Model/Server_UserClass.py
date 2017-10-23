class User:

    def __init__(self,id_, user_,nickname_,password_):
        self.id = id_
        self.user = user_
        self.nickname= nickname_
        self.password = password_

    def toString(self):
        return self.id+" "+self.user+" "+self.nickname+" "+self.password