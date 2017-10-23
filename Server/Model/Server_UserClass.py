class User:

    def __init__(self,id_, user_,nickname_,password_):
        self.id = id_
        self.user = user_
        self.nickname= nickname_
        self.password = password_

    def toString(self):
        return_string = "ID: " + str(self.id) + " | User: "+ self.user + " | Nickname: "+ self.nickname + " | Password: "+ self.password
        return return_string