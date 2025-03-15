print(f'{'='*30}')
print(f'{'10 TERMOS DE UMA PA':^30}')
print(f'{'='*30}')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo = termo + (10 -1) * razao

for c in range(termo, decimo + razao, razao):
    print(f'{c} ->', end =' ')

print('ACABOU')
