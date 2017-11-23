print('05/loop3.py')
my_data = [12, 43,  63, 34, 4532, 1, 53]
result = []


while my_data:
    my_min = min(my_data)
    result.append(my_min)
    my_data.remove(my_min)


print(result)
