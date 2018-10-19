p = {25, 28, 587, 985}
print(type(p))

s = set([2, 4, 16, 64, 64, 18, 4, 2])
print(s)

for value in {25, 28, 587, 985}:
    print("{value}".format(value=value))

print(25 in {25, 28, 587, 985})
print(100 not in {25, 28, 587, 985})

s = {25, 28, 587, 985}
s.add(25)
print(s)

s.add(125)
print(s)

s.update([37, 128, 9, 25, 125])
print(s)

#Shallow Copy
k = s.copy()

#Remove 
s.remove(125)
print(s)
s.discard(126)
print(s)

#Set Algebra
a = {25, 30, 35, 40, 45, 50}
b = {10, 20, 30, 40, 50}
c = {50, 100, 150, 200, 250}
d = {50, 100}
e = {11, 22}

#Set Operator
print(a.union(b))
print(a.intersection(b))
print(c.difference(a))
print(a.symmetric_difference(b))
print(d.issubset(c))
print(c.issuperset(d))
print(d.isdisjoint(e)) 