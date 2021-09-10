from random import randint
from timeit import timeit

max_size = 100
num_ex = 10_000


def bubble(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array


def bubble_no_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array


numbers = [randint(-100, 100) for _ in range(max_size)]
print(numbers)
print(bubble(numbers))

time1 = timeit(f'bubble({numbers})',
              setup='from __main__ import bubble',
              number=num_ex)
time2 = timeit(f'bubble_no_smart({numbers})',
              setup='from __main__ import bubble_no_smart',
              number=num_ex)
print(time1)
print(time2)
