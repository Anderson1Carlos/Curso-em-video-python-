# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da progressão aritmética: '))
decimo = termo + (10-1) * razao
while termo != decimo + razao:
    print(f'{termo}', end=" → ")
    termo += razao
print('ACABOU')
