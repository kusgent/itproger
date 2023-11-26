n = int(input("Введите длину списка: "))

user_list = []

i = 0
while i < n:
    string = "Введите элемент списка #" + str(i) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)
