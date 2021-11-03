# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (descosiderando o flag).
num = 1000
acu = 0
soma = 0
while num != 999:
    num = int(input('Informe um número (999 para finalizar a execução do programa): '))
    if num != 999:
        acu += 1
        soma += num
if acu >= 2:
    print(f'Ao todo foram fornecidos {acu} números que resultou na soma de {soma}.')
else:
    print(f'Ao todo foi fornecido {acu} número.')





