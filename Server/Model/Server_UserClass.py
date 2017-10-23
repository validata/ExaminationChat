class User:

    def __init__(self,id_, username_,nickname_,password_):
        self.id = id_
        self.username = username_
        self.nickname= nickname_
        self.password = password_

    def toString(self):
        return_string = "ID: " + str(self.id) + " | Username: "+ self.username + " | Nickname: "+ self.nickname + " | Password: "+ self.password
        return return_string