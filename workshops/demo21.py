# Define Class
class User:
    username = ""
    password = ""

    """
    def __init__(self):
        self.username = "admin"
        self.password = "1234"
        self.print()
    """

    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password
        self.print()

    def print(self):
        print("created : {}, {}".format(self.username, self.password))


# Create an object from above class
user1 = User("lek", "555")
user2 = User()
