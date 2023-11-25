numbers = [3, 6, 1]

numbers.append(101)
numbers.append(False)
# numbers.append("Yes")
numbers.insert(1, 5)
numbers.extend([1, 2, 3])
# numbers.sort()
numbers.reverse()
numbers.pop()
numbers.pop(1)
numbers.remove(False)
# numbers.clear()

print(numbers)
print(numbers.count(1))
print(numbers.count("True"))
print(len(numbers))
