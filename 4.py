n = int(input('Введите количество элементов: '))
i = 0
range_num = 1
sum = 0
while i < n:
    sum += range_num
    range_num /= -2
    i += 1

print(f'Сумма {sum}')
