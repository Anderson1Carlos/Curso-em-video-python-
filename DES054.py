# Crie um programa leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
menor = 0
for c in range(1, 8):
    nasc = int(input('Informe sua data de nascimento: '))
    if ano_atual - nasc < 18:
        menor += 1
print(f'Total de menor de idade: {menor}\nTotal de maior de idade: {7 - menor}')
