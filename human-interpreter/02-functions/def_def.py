print(1)
def f(x):
    print(3)

    def f2(a):
        print(6)
        return a + x

    return f2

add_2 = f(2)
add_3 = f(3)
add_4 = f(4)
print(add_2(2))
