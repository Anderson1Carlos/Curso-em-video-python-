# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares. Se o valor digitado for impar, desconsidere-o.
aku = 0
cont = 0
cont_par = 0
b = int(input('Quantas número pretende digitar? '))
for c in range(1, b+1):
    num = int(input('Informe um número: '))
    cont += 1
    if num % 2 == 0:
        cont_par += 1
        aku += num
print(f'O valor da soma de {cont} números, onde {cont_par} são pares, foi de: {aku} ')
