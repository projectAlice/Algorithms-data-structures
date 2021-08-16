print('Ведите 3 разных числа:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

mid = a + b + c - max(a, b, c) - min(a, b, c)

print(f'Число {mid} - среднее')
