# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.
km = int(input('Informe o km percorrido: '))
if km <= 200:
    print(f'Total à pagar: R$ {km*0.50:.2f}')
else:
    print(f'Total à pagar: R$ {km*0.45:.2f}')