nove_qtd = tres_index = 0
pares = []


num = int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: '))

for c in num:
    if c == 9:
        nove_qtd += 1
    if c == 3:
        tres_index = num.index(3)
print('Número par: ', end=' ')
for c in num:
    if c % 2 == 0:
        print(c, end='|')
print('\n')        
        
        
print(f'O número nove apareceu {nove_qtd} vez(es)')
if tres_index == 0:
    print(f'O três não foi digitado.')
else:
    print(f'O número três apareceu no index {tres_index}')
