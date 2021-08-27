import random

r = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = -99
min_index_2 = -98

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента в массиве {r[min_index_1]} и {r[min_index_2]}')

