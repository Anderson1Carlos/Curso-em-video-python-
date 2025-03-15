print(f'{'='*30}')
print(f'{'10 TERMOS DE UMA PA':^30}')
print(f'{'='*30}')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo = termo + (10 -1) * razao
novos_termos = 1
acumuladora = 0

while novos_termos != 0:
    while termo != decimo + razao: 
        print(f'{termo} ->', end =' ')
        termo += razao
        acumuladora += 1
    print('PAUSA')
    novos_termos = int(input('Quantos termos você quer mostrar a mais? '))
    decimo = termo + (novos_termos -1) * razao
    
 
print(f'Progressão finalizadas com {acumuladora} termos mostrados.')
