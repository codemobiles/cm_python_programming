# List
dataList1 = ["angular", "vuejs", "react"]  # implicit
dataList2: list = ["angular", "vuejs", "react"]  # explicit
dataList3 = list(("angular", "vuejs", "react"))  # constructor

print(dataList1)
print(dataList2)
print(type(dataList2))
print(dataList3)

extraArray = ["raspberrypi", "flutter"]
dataList1.append("python")
dataList1.extend(extraArray)
dataList1.insert(1, "lek")
dataList1.extend(dataList2)
dataList1.remove("vuejs")
dataList1.remove("vuejs")
dataList1.pop()
dataList1.pop()
# dataList1.clear()
# del dataList1
print(dataList1)
print(dataList1[2])
