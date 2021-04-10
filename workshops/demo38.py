# * Asterisks
numbers = [1, 2, 3]
anotherNumbers = [4, 5, 6]
allNumbers = [*numbers, *anotherNumbers]
print(allNumbers)

colorSet1 = {"Red": "#F00", "Green": "#0F0"}
colorSet2 = {"Yellow": "#FF0", "Blue": "#00F"}
allColors = {**colorSet1, **colorSet2}
print(allColors["Yellow"])

print(allNumbers)
print(allNumbers[0], allNumbers[1])
print(1, 2)
print(*allNumbers)


def show(msg1, msg2, msg3):
    print(msg1)
    print(msg2)
    print(msg3)


show(*["Angular", "Vue", "React"])


def test(*messages):
    print(len(messages))
    print(messages[1])


test("lek", "kan", "dotone")
