num1 = 496
num2 = 285

print(id(num1))
print(id(num2))

num1 = num2
print(id(num1) == id(num2)) #True

numList = [2, 4 ,6 ,8]
numList1 = numList
print(id(numList) == id(numList1)) #True

m = [9, 15, 24]
def modify_list(k):
    k.append(39)
    print("K=", k)

modify_list(m)
print("m=", m)

f = [25, 28, 78]
def replace(g):
    g = [25, 87, 88]
    print("g=", g)

replace(f)
print("f=", f)

def add(a, b):
    return a + b

print(add(5, 7))
print(add(3.1, 2.4))
print(add("news", " paper"))
print(add([1,6], [21, 107]))