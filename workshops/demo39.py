# ** Double Asterisks

def login(username, password):
    print("{0}, {1}".format(username, password))


login("admin", "1234")

acc = {"username": "root", "password": "555"}
login(acc["username"], acc["password"])
login(**acc)