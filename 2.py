import math


def with_er(i):
#без использования алгоритма «Решето Эратосфена»
    num_prime = [2]
    number = 3
    while len(num_prime) < i:
        flag = True
        for j in num_prime .copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            num_prime.append(number)
        number += 1
    return num_prime [-1]


def er(i):
#Функция поиска i-го простого числа,используя алгоритм «Решето Эратосфена»
    i_max = prime_counting_function(i)
    num_prime  = [_ for _ in range(2, i_max)]

    for number in num_prime:
        if num_prime.index(number) <= number - 1:
            for j in range(2, len(num_prime)):
                if number * j in num_prime [number:]:
                   num_prime .remove(number * j)
        else:
            break
    return num_prime[i - 1]


def prime_counting_function(i):

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


user_number = int(input('Введите номер по счету простого числа: '))
print(with_er(user_number))

print('Алгоритм  без использования алгоритма «Решето Эратосфена»')
print(
    f'with_er{(user_number)} - {user_number} \
по счёту простое число'
)

print('Алгоритм  с использованием алгоритма «Решето Эратосфена»')
print(
    f'{er(user_number)} - {user_number} по счёту простое число'
)
