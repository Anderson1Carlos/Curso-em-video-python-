velo = int(input('Informe a velocidade do carro: KM/H '))
if velo > 80:
    print(f'Você foi multado!\nValor da multa: R${(velo - 80) * 7:.2f}')
