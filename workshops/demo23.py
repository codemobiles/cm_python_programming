# Define Class
class User:
    username = ""
    password = ""

    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

    def __str__(self):
        return "username: {}, password: {}".format(self.username, self.password)

    def print(self):
        print("created : {}, {}".format(self.username, self.password))


# Create an object from above class
user1 = User("lek", "555")
# user1.print()
print(user1)
