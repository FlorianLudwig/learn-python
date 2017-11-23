print('08/04_listcomprehension')

a = [i for i in range(4)]
print(a)

a = [i*2 for i in range(4)]
print(a)

a = [i*2 for i in range(4) if i % 2 == 0]
print(a)
