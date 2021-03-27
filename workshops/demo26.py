# Define Class
class User:
    username = ""
    password = ""

    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

# Inheritance / subclass


class UserV1(User):
    # level = "standard"

    def __init__(self):
        self.level = "standard"

    def clear(self):
        self.username = ""
        self.password = ""

    def __str__(self):
        return "username: {}, password: {}, level: {}".format(self.username, self.password, self.level)


# Create an object from above class
# user = User("lek", "555")
# user.clear()
# print(user)
user = UserV1()
# user.clear()
print(user)
