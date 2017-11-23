print('05/loop1.py')

for i in ['a', 'b', 'c', 'd', 'e']:
    if i == 'b':
        continue

    print(i)

    if i == 'd':
        break

print()

my_data = [12, 43, 63, 34]
for i in range(len(my_data)):
    print("a")

print()

for i in my_data:
    print("a {}!".format(i))
