word = "one, two, three"
catalog = word.split(", ")

for i in range(len(catalog)):
    catalog[i] = catalog[i].capitalize()

print(catalog)

result = ", ".join(catalog)
print(result)
print(type(result))
