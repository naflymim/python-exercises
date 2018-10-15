import math

#Homogeneous immutable sequence of Unicode codepoints (characters)
print(len("Python is awesome language"))
print("New" + "Found" + "Land")

name = ','.join(["New", "Pyhton"])
print(name)
print(name.split(','))

result = "unforgetable".partition("forget")
print(result)

departure, separator, arrival = "London:Edinburgh".partition(":")
print(departure)
print(arrival)

#_ is always used for Dummy/unused variables
origin, _, destination = "Seattle-Boston".partition("-")
print(origin)
print(destination)

strValue = "The age of {0} is {1}".format("Saman", 28)
print(strValue)

strValue = "The age of {name} is {age}".format(name="Saman", age=28)
print(strValue)

pos = (65.2, 23.14, 82.5)
valueStr = "Galactic position X={pos[0]} Y={pos[1]} and Z={pos[2]}".format(pos=pos)
print(valueStr)

valueStr = "Math constants: pi={m.pi: .3f}, e={m.e: 3f}".format(m=math)
print(valueStr)