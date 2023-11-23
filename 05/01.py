num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
num3 = int(input("Введите число: "))
num4 = int(input("Введите число: "))
num5 = int(input("Введите число: "))

if num1 > 2 and num2 > num3 or num4 > num5:
    print("1")
else:
    print("0")

# тернарный оператор
data = input()
number = 5 if data == "Five" else 0
print(number)
