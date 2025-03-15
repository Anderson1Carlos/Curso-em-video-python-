from random import sample

num_aleatorios = ()
maior = menor = 0

populacao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_aleatorios = sample(populacao, 5) 
#Poderia armazernar o randint cinco vezes na tupla

for pos, c in enumerate(num_aleatorios):
    if pos == 0:
        maior = menor = c
    elif c > maior:
        maior = c
    elif c < menor:
        menor = c
#Poderia utilizar as funções max e min

print(num_aleatorios)
print(f'Maior da lista: {maior}\nMenor da lista: {menor}')

