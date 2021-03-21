# Global Variable
tmp1 = "CodeMobiles"
def change():
    # Local Variable
    tmp1 = "Lek"
    print("tmp1 in change function : " + tmp1)


def changeGlobal():
    # Local Variable
    global tmp1
    tmp1 = "Lek"
    print("tmp1 in changeGlobal function : " + tmp1)


print(tmp1)
change()
print(tmp1)

changeGlobal()
print(tmp1)
