km = float(input('Informe a qtd de KM rodado: '))
dia = int(input('Informe a qtd. de dias de alugel: '))
print(f'Diária: +R${dia * 60:.2f} \nKm rodados: +R${km * 0.15:.2f} \nValor Total: R${(dia * 60)+(km * 0.15):.2f}')