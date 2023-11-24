for i in range(1, 11):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

found = None
for i in "hello":
    if i == "l":
        found = True
        break
else:
    found = False

print(found)
