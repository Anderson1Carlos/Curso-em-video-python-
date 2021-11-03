# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Informe um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        cont += 1
    elif num % c != 0:
        print(f'\033[31m{c}\033[m', end=' ')
print('.')
if cont == 2:
    print(f'\n{num} é primo pois foi divísivel {cont} vezes.')
else:
    print(f'\n{num} não é primo pois foi divísivel {cont} vezes.')
