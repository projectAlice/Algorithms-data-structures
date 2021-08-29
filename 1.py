import math
import timeit

def func_1(max_number):
    div_dict = dict()
    result = {}
    for n in range(2, 10):
        result[n] = []
        for f in range(2, 100):
            if f % n == 0:
                result[n].append(f)
    return div_dict

MIN_DIV = 2
MAX_DIV = 9

def func_2(max_number):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = max_number // div

    return div_dict

NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000    
time1 = timeit.timeit (f'func_1({TEST_VALUE})',
                      setup='from __main__ import func_1',
                      number=NUMBER_EXECUTIONS)
time2 = timeit.timeit (f'func_2({TEST_VALUE})',
                      setup='from __main__ import func_2',
                      number=NUMBER_EXECUTIONS)
                    

print (f'Алгоритм №2 быстрее алгоритма №1 в {round(time1/time2, 2)} раз') 
