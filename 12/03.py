def minimal(list_numbers):
    min_number = list_numbers[0]
    for i in range(1, len(list_numbers)):
        if list_numbers[i] < min_number:
            min_number = list_numbers[i]
    return min_number


print(minimal([5, 6, 9, 0, 1, 3, -7]))
