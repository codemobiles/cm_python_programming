dictionaryData = {"dog": "หมา", "cat": "แมว", "cat": "แมวแมว", }
print(dictionaryData)
print(dictionaryData["cat"])
print(dictionaryData.get("dog"))
print(dictionaryData.keys())

dictionaryData["bird"] = "นก"
print(dictionaryData)

dictionaryData.pop("bird")
del dictionaryData["dog"]
print(dictionaryData)
