tier_a = ( 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará',
           'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza',
            'Grêmio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras',
            'Santos', 'Sport', 'São Paulo', 'Vasco', 'Vitória')
print('Os cinco primeiros times: ')
for c in range(0 ,5):
    print(f'{c + 1}º - {tier_a[c]}')
print('-'*30)

print('Os últimos colocados: ')
for c in range(19, 15, -1):
    print(f'{c + 1}º - {tier_a[c]}')
print('-'*30)   

print('Times em ordem alfabética: ')
for c in range(0, len(tier_a)):
    print(f'{c + 1}º - {sorted(tier_a)[c]}')
print('-'*30)

print('Qual a posição da Sport? ')
for pos, c in enumerate(tier_a):
    if c == 'Sport':
        print(f'{pos + 1}º')