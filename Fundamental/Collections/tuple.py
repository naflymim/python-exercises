#Tuples in Python are immutable sequence of arbitary objects. Once created, 
# the objects within then cannot be removed, replaced and cannot be added 
myTuple = ("Norway", 4.953, 3)
print(myTuple)
print(type(myTuple))

print(myTuple[2])

for item in myTuple:  
    print(item)

for item in myTuple:  
    print(type(item))

print(len(myTuple))

myTuple = myTuple + (3365.25, "Sample")
print(myTuple)

myTuple = myTuple * 2
print(myTuple)

a = ((220, 284), (1184, 1210), ("Test", "Python", 285))
print(a[2])
print(type(a[2]))
print(a[2][1])
print(type(a[2][1]))

def minmax(items):
    return min(items), max(items)

print(minmax([83, 33, 84, 32, 85, 31, 86]))

#Tuple and unpacking 
#Tuples are useful for mutiple returns values
lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
print(lower)
print(upper)