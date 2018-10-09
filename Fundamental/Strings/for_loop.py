cities = ["Matara", "Kandy", "Colombo", "Nuwareliya", "Galle", "Gampaha"]
for city in cities:
    print(city)

#iterate range
for number in range(1, 20, 5):
    print(number)

#iterate dictionaries
telephoneDir = {'Nafly': '125-899-5580', 'Bob': '125-258-8859', 'Eve': '145-875-5896'}
for tel in telephoneDir:
    print(tel, telephoneDir[tel])

#iterate two for
a = [(x, y) for x in range(1, 3) for y in range(x, 5)]
print(a)

a = [(x, y) for x in range(1, 10) for y in range(1, 5) if x == y]
print(a)