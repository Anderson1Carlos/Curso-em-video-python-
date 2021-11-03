# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. para salários superiores a R$1.250,00, calcule um aumento da 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Informe seu salário: '))
if sal > 1250:
    print(f'Salário atual: {sal:.2f}\nSalário pós aumento: {sal*(10/100)+sal:.2f}')
else:
    print(f'Salário atual: {sal:.2f}\nSalário pós aumento: {sal*(15/100)+sal:.2f}')