def some_generator():
  print(2)
  print((yield 3))
  print(4)
  print((yield 5))


print(8)
g = some_generator()
print(10)
print(g.send(None))
print(12)
print(g.send(13))
