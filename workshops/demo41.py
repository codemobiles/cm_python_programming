tmp1 = True
tmp2 = False
# tmp3 = True
tmp4: str = None
# tmp4: str = "Lek"

print(tmp1)
print(tmp2)

try:
    print(tmp3)
except:
    print("tmp3 undefined")

if tmp4 is None:
    print("tmp4 is None")
else:
    print(tmp4)

print(type(None))
