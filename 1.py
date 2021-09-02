import collections
import random


def sum_tuple(numbers):
    '''tuple --> sum'''

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

base_enterprise = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за I-ый квартал: '))
    profit_q2 = int(input('Прибыль за II-ой квартал: '))
    profit_q3 = int(input('Прибыль за III-ий квартал: '))
    profit_q4 = int(input('Прибыль за IV-ый квартал: '))
    base_enterprise[name] = Enterprise(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4
    )


total_profit = ()

for name, profit in base_enterprise.items():
    print(f'Прибыль предприятия  {name}  за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(base_enterprise)
print(f'Средняя прибыль для всех предприятий за год  - {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_enterprise.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')
        
print('Предприятия, у которых прибыль ниже среднего:')

for name, profit in base_enterprise.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')


