# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
termos = int(input('Informe quantos termos: '))
counter = termos
x = 0
y = 1
z = x + y
cont = 0
while cont <= termos:
    cont += 1
    while cont <= 1:
        print(f'{x}', end=' --> ')
        cont += 1
    while cont <= 2:
        print(f'{y}', end=' --> ')
        cont += 1
    while 3 <= cont <= termos:
        print(f'{z}', end=' --> ')
        x = y
        y = z
        z = x + y
        cont += 1
    print('Acabou')








