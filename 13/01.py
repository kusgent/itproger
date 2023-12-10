data = input("Введите текст: ")

file = open('text.txt', 'a')

file.write(data + "\n")

file.close()
