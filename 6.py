import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index = 0
max_index = 0
step = 1
sum = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)
    elif r[max_index] < i:
        max_index = r.index(i)

if max_index - min_index < 0:
    step = -1

for i in r[min_index + step:max_index:step]:
    sum += i

print(
        f'Сумма элементов между минимальным элементом -{r[min_index]}',
        f' и максимальным элементом - {r[max_index]} равна {sum}'
        )
