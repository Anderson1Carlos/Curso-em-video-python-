soma = 0
for c in range(0, 6):
    num = int(input(f'Informe o {c + 1}º número: '))
    if num % 2 == 0:
        soma += num
print('Soma final dos números digitados: ', soma)
