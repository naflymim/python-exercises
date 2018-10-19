s = "Show how to index into sequence".split()
print(s)

print(s[0])
print(s[-6])

#Slicing 
print(s[1: 4])
print(s[3:])
print(s[:3])
print(s[:])
print(s[::-1])


full_slice = s[:]
print(full_slice)
print(full_slice is s)
print(full_slice == s)

copyList = s.copy()
print(copyList)
print(copyList is s)
print(copyList == s)

#List Repetition
c = [21, 37]
print(c * 4)
print([0] * 9)

rangeList = [[-1, +1]] * 5
print(rangeList)
rangeList[3].append(7)
print(rangeList)

#Searching on the list
w = "the quick brown fox jumps over the lazy dog".split()

index = w.index("jumps")
print(w[index])

print(w.count("the"))
print("the" in w)
print("unicorn" not in w)

#Delete an item from the list
u = "jackdwas love my big sphinx of quartz".split()
print(u)

del u[3]
print(u)

u.remove("jackdwas")
print(u)

del u[u.index("sphinx")]
print(u)

#Inser into a list
a = "I accidentlly the whole universe".split()
a.insert(2, "destroyed")
print(a)
print(" ".join(a))


#Growing Lists
m = [2, 1 ,3]
n = [4, 7 ,11]
k = m + n
print(k)

k += [18, 29, 27] 
print(k)

k.extend([25, 48, 55])
print(k)

#Reversing and Sorting 
g = [1, 11, 21, 1211, 112111]
g.reverse()
print(g)

g.sort()
print(g)

g.sort(reverse=True)
print(g)

h = "not perplexing do handwriting family where I illegibly know doctors".split()
h.sort(key=len)
print(h)
print(" ".join(h))

x = [4, 9, 2, 1]
y = sorted(x)

print(x)
print(y)

x = [4, 9, 2, 1]
y = reversed(x)

print(x)
print(list(y))