# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7.00 por cada km acima do limite.
vel = int(input('Velocidade do carro (km/h): '))
if vel > 80:
    print(f'Você foi multado por excesso de velocidade. O custo da multa foi: R$ {(vel-80)*7:.2f}')
else:  # Eu poderia não ter usado esse else.
    print('Parabéns, você estava dentro do limite de velocidade.')
