# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
resp = ' '
while resp[0] not in 'N':
    termo = int(input('Informe o primeiro termo: '))
    razao = int(input('Informe a razão da progressão aritmética: '))
    decimo = termo + (10-1) * razao
    while termo != decimo + razao:
        if termo == decimo:
            print(f'{termo}.')
        elif termo != decimo + razao:
            print(f'{termo}', end=" → ")
        termo += razao
    resp = input('Deseja ver mais termos? Sim [S] ou Não [N]? ').strip().upper()[0]
    if resp not in 'SNsn':
        resp = input('Erro! Responda com "S" para sim ou "N" para não: ')
print('Valeu, Até a próxima!')
