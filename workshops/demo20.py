# Define Class
class User:
    username = ""
    password = ""

    def print(self):
        print("from self : {}, {}".format(self.username, self.password))


# Create an object from above class
user = User()
user.username = "root"
user.password = "1234"

print("{}, {}".format(user.username, user.password))
user.print()
