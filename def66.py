contadora = acumuladora = 0

while True:
    contadora += 1
    valor = int(input('Digite um valor (999 para sair): '))
    if valor != 999:
        acumuladora += valor
    elif valor == 999:
        break
print(f'A soma dos {contadora} valores foi {acumuladora}')
