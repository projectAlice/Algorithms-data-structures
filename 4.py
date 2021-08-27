import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

max_index = 0
for i in r:
    if r.count(max_index) < r.count(i):
        max_index = r.index(i)

print(f'Число {r[max_index]}, встречается чаще всего - {r.count(max_index)} раз (а) ')
