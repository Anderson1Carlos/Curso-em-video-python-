from random import randint
from time import sleep
from os import system

print('-='*30)
print(f'{'PAR OU IMPAR':^60}')
print('-='*30)

players = []
soma = 0

while True:
    valor = int(input('Informe seu valor: '))
    cpu = randint(0, 10)
    par_impar = input('Par ou Ímpar? ').upper().strip()
        
    resultado = (cpu + valor) % 2


    if resultado == 0 and par_impar[0] in 'Pp':
        print('-'*30)
        print(f'Você jogou {valor} e o computador {cpu}. Total de {valor + cpu} DEU PAR')
        print('-'*30)
        print('Você VENCEU!')
            

        
    elif resultado == 0 and par_impar[0] in 'IiÍí':
        print('-'*30)
        print(f'Você jogou {valor} e o computador {cpu}. Total de {valor + cpu} DEU PAR')
        print('-'*30)
        print('Você PERDEU!')
        

    elif resultado != 0 and par_impar[0] in 'Pp':
        print('-'*30)
        print(f'Você jogou {valor} e o computador {cpu}. Total de {valor + cpu} DEU ÍMPAR')
        print('-'*30)
        print('Você PERDEU!')
        

    elif resultado != 0 and par_impar[0] in 'IiÍí':
        print('-'*30)
        print(f'Você jogou {valor} e o computador {cpu}. Total de {valor + cpu} DEU ÍMPAR')
        print('-'*30)
        print('Você VENCEU!')
   
    resp = input('Quer jogar novamente? [S/N]: ').upper().strip()
    if resp[0] in 'Ss':
        print('Um momento...')
        sleep(1)
        system('clear')
    elif resp[0] in 'Nn':
        print('OK. Fechando...')
        sleep(1)
        break
    elif resp[0] not in 'Nn' or 'Ss':
        print('Entrada inválida')
        resp = input('Quer jogar novamente? [S/N]: ').upper().strip()

    

            

       
       



     
        

    
    
    
    

