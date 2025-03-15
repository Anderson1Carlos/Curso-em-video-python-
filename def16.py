from emoji import emojize
from math import trunc
num = float(input(emojize(':man_tipping_hand: Informe um número decimal: ')))
print(f'Parte inteira: {trunc(num)}')
print(f'Parte inteira: {num:.0f}') # Essa função de formatar o número não trunca e arredonda.
print(f'Parte inteira: {int(num)}')



