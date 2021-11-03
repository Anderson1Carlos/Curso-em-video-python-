#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('_'*20)
print(' LOCADORA A VIAGEM ')
print('-'*20)
km = float(input('Quantos km foram gastos? '))
dia = int(input('Informe a quantidade de dias gastos: '))
totalkm = km * 0.15
totaldia = dia * 60
print(f"Gastos conforme km's rodados: R${km * 0.15:.2f}\nGastos conforme dias de locação: R${dia * 60}\nTotal a pagar: R${totaldia+totalkm}")
adorno = ' FIM '
print(f'{adorno:-^20}')