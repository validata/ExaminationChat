from Server.Model.Server_UserClass import User
import unittest

User1 = User(1,'MyName','MyNickname','MyPassword')
User2 = User(2,'MyName2','MyNickname2','MyPassword2')

class Tester(unittest.TestCase):
    def test_id(self):
        id_to_test = int(User1.id)
        self.assertGreater(id_to_test, 0, msg="ID is less than 1")

if __name__ == '__main__':
    unittest.main()