N = 4

matrix = []

for i in range(N):
    matrix.append([])
    sum = 0
    for n in range(N):
        user_number = int(input(f'Введите элемент {i+1} и {n+1} столбца: '))
        sum += user_number
        matrix[i].append(user_number)

    matrix[i].append(sum)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))
