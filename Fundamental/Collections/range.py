myRange = range(5)
print(type(myRange))

for i in myRange:
    print(i)

print('')
print('')

for i in range(5, 10):
    print(i)

myRangList = list(range(0, 10))
print(myRangList)

myRangList = list(range(0, 10, 2))
print(myRangList)

print('')

t = [6, 372, 866, 148, 998]
for p in enumerate(t):
    print(p)

for index, item in enumerate(t):
    print("index={index}, item={item}".format(index=index, item=item))
   