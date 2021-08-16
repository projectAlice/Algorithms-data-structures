print('Ведите две прописные буквы латинского алфавита:')
let1 = input('let1 = ')
let2 = input('let2 = ')

pos_let1 = ord(let1) - 64
pos_let2 = ord(let2) - 64
distance = abs(pos_let1 - pos_let2) - 1
print(f'Буква "{let1}" {pos_let1}-я в алфавите\n'
      f'Буква "{let2}" {pos_let2}-я в алфавите\n'
      f'Между буквами {distance} букв')
