# Define Class
class User:
    username = ""
    password = ""

    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

    @staticmethod
    def test():
        print("1234")


User.test()
