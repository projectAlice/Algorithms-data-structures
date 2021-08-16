x = 5
y = 6 
bit_and = x & y
bit_or = x | y
bit_xor = x ^ y
bit_right = x>>2
bit_left = x<<2

print(f'Выполним логические побитовые операции над числами 5 и 6:\n'
      f'5 & 6 = {bit_and}\n'
      f'5 | 6 = {bit_or}\n'
      f'5 ^ 6 = {bit_xor}')

print(f'Выполним над числом 5 побитовый сдвиг вправо на два знака: \n'
       f'5>>2 ={bit_right}\n')

print(f'Выполним над числом 5 побитовый сдвиг влево на два знака: \n'
       f'5<<2 ={bit_left}\n')
