from time import sleep
from os import system

maior_id = homens = novinha = 0

while True:
    print('-'*30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('-'*30)

    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()[0]

    if idade >= 18:
        maior_id += 1
    if sexo[0] in 'Mn':
        homens += 1
    if sexo[0] in 'fF' and idade < 20:
        novinha += 1

    
    resposta = input('Quer continuar? [S/N] ').strip().upper()
    while resposta[0] not in 'SsNn':
        resposta = input('Entrada inválida! Quer continuar? [S/N] ')
    if resposta[0] in 'Nn':
        print('Ok! Fechando...')
        sleep(1)
        break
    system('cls')

print(f'''
Total de pessoas com mais de 18 anos: {maior_id}
Ao todo temos {homens} homem(s) cadastrados
E temos {novinha} mulher(es) com menos de 20 anos       
''')


