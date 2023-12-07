data = set('hello')
data_new = {1, 2, 3, 1, 2, 3}

print(data)
print(data_new)

data.add(35)
data_new.update(['test', False, 777, 777])

print(data)
print(data_new)

data_new.remove(777)
data_new.pop()

print(data_new)

data.clear()

print(data)

nums = [5, 5, 6, 7, 5]
nums = set(nums)

print(nums)
