def sum_num(num):
    sum = 0
    for f in num:
        sum += int(f)
    return sum


list_num = [i for i in input('Введите числа:').split()]

max_num = 0
max_sum = 0
for i in list_num:
    if sum_num(i) > max_sum:
        max_num = i
        max_sum = sum_num(i)

print(f'У числа {max_num} наибольшая сумма цифр - {max_sum}')
