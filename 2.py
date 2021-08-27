import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {r}')
index_ev = []

for n in r:
    if n % 2 == 0:
        index_ev.append(r.index(n))

print(f'Индексы чётных элементов первого массива: {index_ev}')
