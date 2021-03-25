# Define Class
class User:
    username = ""
    password = ""

    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

# Inheritance / subclass


class UserV1(User):
    def clear(self):
        self.username = ""
        self.password = ""

    def __str__(self):
        return "username: {}, password: {}".format(self.username, self.password)


# Create an object from above class
user = User("lek", "555")
# user.clear()
print(user)
user = UserV1("lek", "555")
# user.clear()
print(user)
