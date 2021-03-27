# Define Class
class Calculator:

    def divide(self, a, b):
        return a / b


c = Calculator()

try:
    print(c.divide(1, 3))
    dataArray = [1, 2, 3]
    print(dataArray[3])
except ZeroDivisionError:
    print("invalid data due to zero division")
except IndexError:
    print("invalid data due to index out of boundary")
except:
    print("invalid data")
