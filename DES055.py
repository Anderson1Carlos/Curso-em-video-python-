# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesos lidos.
maior = 0
x = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Informe o peso: '))
    if c == 1:
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'Peso maior: {maior}Kg\n'
      f'Peso menor: {menor}kg')


