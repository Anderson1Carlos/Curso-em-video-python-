num = int(input('Informe um número entre 0 a 9999: '))
print(f'Unidade: {num // 1 % 10} \nDezena: {num // 10 % 10}\nCentena: {num // 100 % 10}\nMilhar: {num // 1000 % 10}')