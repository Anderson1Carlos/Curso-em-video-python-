# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Informe o número: '))
n2 = int(input('Informe o número: '))
n3 = int(input('Informe o número: '))
if n1 > n2 and n1 > n3:
    print(f'Maior: {n1}')
if n2 > n1 and n2 > n3:
    print(f'Maior: {n2}')
if n3 > n1 and n3 > n2:
    print(f'Maior: {n3}')
if n1 < n2 and n1 < n3:
    print(f'Menor: {n1}')
if n2 < n1 and n2 < n3:
    print(f'Menor: {n2}')
if n3 < n1 and n3 < n2:
    print(f'Menor: {n3}')
