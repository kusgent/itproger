file = open('text.txt', 'r')

# print(file.read(5))
# print(type(file.read()))

for line in file:
    print(line, end="")

file.close()
