country = {'code': 'RU', 'name': 'Russia', 'population': 145}
country_test = dict(code='RU', name='Russia', population=145)

print(country)
print(country['code'])
print(country_test)
print(type(country))
print(type(country_test))

print(country.items())

for key, value in country.items():
    print(key, '-', value)
