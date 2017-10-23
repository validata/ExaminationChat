from Server.Model.Server_UserClass import User

User1 = User(1,'Me','MyNickname','MyPassword')
print(User1.toString())

class TestStringMethods(unittest.TestCase):

    def banned_or_not(self):
        self.assertTrue()

if __name__ == '__main__':
    unittest.main()