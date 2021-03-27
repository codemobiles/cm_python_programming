# Define Class
class User:
    username = ""
    password = ""

    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

    def clear(self):
        print("clear")
        self.__privateClear()

    #  private function
    def __privateClear(self):
        print("private clear")


user = User()
user.clear()
# user.__privateClear()
