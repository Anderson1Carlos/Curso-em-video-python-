# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
adorno = ' Calculadora de aumento '
adorno1 = ' Fim '
print(f'{adorno:*^32}')
sal = float(input('Digite seu salário: R$ '))
aum = int(input('Digite o valor do aumento (%): '))
after = sal*(aum/100)
print(f'Valor do salário pós desconto: {sal+after:.2f}')
print(f'{adorno1:*^32}')

