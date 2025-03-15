
fatorando = int(input('Informe o fatorando: '))
auxiliar = fatorando
fatoracao = 1

print(f'{fatorando}! = ',end='')

while auxiliar > 0:
    fatoracao *= auxiliar
    if auxiliar > 1:
        print(f'{auxiliar} x ', end='')
    else:
        print(f'{auxiliar} = ', end='')
    auxiliar -= 1
print(f'{fatoracao}')