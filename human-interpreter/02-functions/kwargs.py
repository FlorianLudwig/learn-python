def f(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)


f(1, 2, 3, 4)

a = [4, 5, 6, 7]
f(5, *a)


k = {'a': 2, 'b': 4}
f(**k)


k = {'c': 1, 'a': 2, 'b': 4}
f(**k)

f(b=11, a=22)
