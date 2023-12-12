try:
    x = int(input("Введите число: "))
    x /= 5
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("Введено НЕ число")
else:
    print("Результат:", x)
finally:
    print("Программа завершена.")
