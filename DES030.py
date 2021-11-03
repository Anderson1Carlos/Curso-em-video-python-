# Crie um programa que leia um número inteiro e mostre na tela se ela é PAR ou IMPAR.
num = int(input('Informe um número: '))
if num % 2 == 0:
    print(f'{num} é PAR.')
else:
    print(f'{num} é IMPAR.')