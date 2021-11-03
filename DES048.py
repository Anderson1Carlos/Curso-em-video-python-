# Faça um program que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
cont = 0
soma = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        cont += 1
        soma += c
print(f'Dos {cont} valores solicitados, a soma total foi: {soma}.')
