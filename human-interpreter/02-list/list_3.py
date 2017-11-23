a = [1, 2, 3]

print(a[0])
print(a[1:])
print(a[:])

b = a
a.append(4)
print(a)
print(b)

c = a
a = 1
print(a)
print(c)
