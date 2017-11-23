print('00/def.py')

def f(x):
    return x

print(f(1))


def f(x):
    x * 2

print(f(2))


g = f
print(g(1))

def f():
    return None

print(g())

del f
