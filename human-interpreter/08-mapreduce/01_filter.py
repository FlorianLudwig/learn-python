print('08/01_map.py')

def is_even(i):
    return i % 2 == 0


for i in filter(is_even, range(10)):
    print(i)
