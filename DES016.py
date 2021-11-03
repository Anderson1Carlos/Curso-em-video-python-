# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Informe um número decimal: '))
print(f'Porção inteira de {num}: {trunc(num)}')  # Também posso utiliza a função interna int().