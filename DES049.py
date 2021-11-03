# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Informe o operando da tabuada: '))
ope = int(input('Informe o operador da tabuada: [1] adição [2] subtração [3] multiplicação [4] divisão >>> '))
for c in range(1,11):
    if ope == 1:
        print(f'{num: ^3} + {c: ^3} = {num + c}')
    elif ope == 2:
        print(f'{num: ^3} - {c: ^3} = {abs(num - c)}')
    elif ope == 3:
        print(f'{num: ^3} * {c: ^3} = {num * c}')
    elif ope == 4:
        print(f'{num: ^3} : {c: ^3} = {num / c:.1f}')
