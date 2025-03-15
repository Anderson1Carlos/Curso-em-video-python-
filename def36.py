print('- APROVAÇÃO DE EMPRÉSTIMO -')

#Questionário onde receberemos os dados de entrada
valor_casa = float(input('Informe o valor da casa: R$'))
salario_comprador = float(input('Informe o valor do seu salário: R$'))
anuidade = int(input('Informe em quantos anos quitarás a dívida: '))

#Calcúlo da prestação e da regua salarial que não pode exceder de 30%
regua_salarial = salario_comprador * (30/100)
prestacao = valor_casa / (anuidade*12)

#Estrutura de condição que ira definir a saida final dos dados
if prestacao > regua_salarial:
    print(f'Valor da casa: R${valor_casa:.2f}\nValor das parcelas mensais: R${prestacao:.2f} x{anuidade*12}\nStatus: Negado!')
else:
    
    print(f'Valor da casa: R${valor_casa:.2f}\nValor das parcelas mensais: R${prestacao:.2f} x{anuidade*12}\nStatus: Aprovado!')



