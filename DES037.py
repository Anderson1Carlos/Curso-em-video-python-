# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal
num = int(input('Informe um número de base decimal: '))
base = int(input('Selecione a base de conversão: [1] binário, [2] octal, [3] hexadecimal >>> '))
if base == 1:
    print(f'{num} >>> {num:b}')  # Bem, eu poderia utilizar a função bin(), porém ela me retorna, antes do número convertido, duas letras 'ob'.
elif base == 2:
    print(f'{num} >>> {num:o}')
elif base == 3:
    print(f'{num} >>> {num:x}')  # O x minúsculo me retorna um número hexadecimal minúsculo. Já o maiúsculo segue a lógica.
else:
    print(f'Essa opção não está disponível. Tente novamente!')