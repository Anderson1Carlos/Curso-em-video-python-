salario = float(input('Informe seu salário atual: '))
if salario > 1250:
    print(f'Salário antigo: R$ {salario:.2f}\nSalário Pós-ajuste (10%): R$ {salario * (10/100) + salario:.2f}')
else:
    print(f'Salário antigo: R$ {salario:.2f}\nSalário Pós-ajuste (15%): R$ {salario * (15/100) + salario:.2f}')
            
     
