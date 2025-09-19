candidates = [0, 1, -1, "", "0", [],[0], {}, {"a":1} ]
for m in candidates:
    print(repr(m), "-->", bool(m))
age = 36
if age >= 18:
    print("adult")
else:
    print("teenager")


