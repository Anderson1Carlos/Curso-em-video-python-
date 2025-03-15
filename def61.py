print(f'{'='*30}')
print(f'{'10 TERMOS DE UMA PA':^30}')
print(f'{'='*30}')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))


contadora = 0

while contadora < 10:
    
    print(f'{termo} ->', end =' ')
    termo += razao
    contadora += 1
    
print('ACABOU')