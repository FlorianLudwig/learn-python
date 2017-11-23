def add(value):
    print(2)

    def decorator(func):
        print(5)

        def wrapper(x):
            print(8)
            re = func(x)
            return re + value

        return wrapper

    return decorator


@add(1)
def f():
    print('f 18')
    return 41


f42 = f()
print(f42())
