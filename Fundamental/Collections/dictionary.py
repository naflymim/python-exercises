from pprint import pprint as pp

urls = {'Google': 'https://www.google.com/', 
        'Pluralsight': 'https://pluralsight.com/', 
        'Sixty North': 'https://sixty-north.com/',
        'Microsoft': 'https://www.microsoft.com/'}

print(urls['Microsoft'])
print(urls['Pluralsight'])

#Converting
name_and_age = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Danial', 33)]
d = dict(name_and_age)
print(d)

#Creating 
phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo')
print(phonetic)

#updating 
phonetic.update(dict(a='alfa-u', f='fun', g='goat', h='hello'))
print(phonetic)

#Iteratable
for key in phonetic:
    print("{key} => {value}".format(key=key, value=phonetic[key]))

for value in phonetic.values():
    print("{value}".format(value=value))

for key in phonetic.keys():
    print("{key}".format(key=key))

for key, value in phonetic.items():
    print("{key} => {value}".format(key=key, value=value))

print(pp(phonetic))

