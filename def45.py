from random import randint
from time import sleep
player = int(input('''
Suas opções:
                    
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
                   
Qual a sua opção? '''))

cpu = randint(0,2)
match player:
    case 0:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('PO.')
        if cpu == 1:
            print('Você Perdeu! CPU: Papel vs. PLAYER: Pedra')
        elif cpu == 2:
            print('Você Ganhou! CPU: Tesoura vs. PLAYER: Pedra')
        else:
            print('Empate! CPU: Pedra vs. PLAYER: Pedra')
    case 1:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('PO.')
        if cpu == 2:
            print('Você Perdeu! CPU: Tesoura vs. PLAYER: Papel')
        elif cpu == 0:
            print('Você Ganhou! CPU: Pedra vs. PLAYER: Papel')
        else:
            print('Empate! CPU: Papel vs. PLAYER: Papel')
    case 2:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('PO.') 
        if cpu == 0:
            print('Você Perdeu! CPU: Pedra vs. PLAYER: Tesoura')
        elif cpu == 1:
            print('Você Ganhou! CPU: Papel vs. PLAYER: Tesoura')
        else:
            print('Empate! CPU: Tesoura vs. PLAYER: Tesoura')
    case _:
            print('Número inválido!')
        
        

