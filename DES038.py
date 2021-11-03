# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais.
num = int(input('Informe um número: '))
num2 = int(input('Informe o segundo número: '))
if num > num2:
    print(f'{num} é maior que {num2}')
elif num < num2:
    print(f'{num} é menor {num2}')
elif num == num2:
    print(f'Ambos são números iguais')