country = {'code': 'RU', 'name': 'Russia', 'population': 145}

print(country['population'])
print(country.get('population'))

# country.clear()
# print(country)

# country.pop('name')
# print(country)

# country.popitem()
# print(country)

print(country.keys())
print(country.values())

country['code'] = 'None'
print(country)
