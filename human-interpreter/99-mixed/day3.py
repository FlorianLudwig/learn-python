print('day3')

def append_list(l):
    l.append([])


def increase(i):
    i += 1


my_list = []
append_list(my_list)
append_list(my_list)
my_list[0].append(1)
print(my_list)

x = 11
increase(x)
print(x)

# assert [] == []


print('3.1')
my_dict = {'a': 1}
increase(my_dict)
print(my_dict)

pow_dict = {}
for i in range(10):
    pow_dict[str(i)] = i**2

print(pow_dict[2])


print('3.2')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


r = Rectangle(10, 20)
print(r.calc_area())


print('3.3')
a = ['My number is {}'.format(i) for i in range(4)]
print('\n'.join(a))


print('3.4')
print([1] * 2)
print(2 * [1])
print('*' * 10)
print(10 * '*')


print('3.5')
d = {'1': 'a', '2': 'b'}
print(1 in d)
print(d.get('2'))
print(d.get('3'))
