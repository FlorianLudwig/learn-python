import functools
print('08/01_map.py')

def sum(x, y):
    return x + y

print(functools.reduce(sum, range(4)))
