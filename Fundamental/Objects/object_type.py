import time

print(type(time))

#attributes an object
#sorted list of module attributes
print(dir(time))

print(type(time.ctime))
print(dir(time.ctime))

print(time.ctime.__name__)
print(time.ctime.__doc__)