# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from emoji import emojize
from time import sleep
from pygame import mixer
mixer.init()
mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/happy-sandbox.wav')
mixer.music.play(loops=-1)
adorno = emojize(':boom:JOGO DA ADIVINHAÇÃO:boom:', use_aliases=True)
print(adorno)
usuario = 1
tent = 0
luck = randint(0,10)
nome = input('>>> Qual seu nome? ').strip().split()
while luck != usuario:
    usuario = int(input(f'Ok! {nome[0]}, de 0 a 10, tente adivinhar:  '))
    print(emojize(':hourglass: Processando...', use_aliases=True))
    sleep(2)
    tent += 1
    if luck != usuario:
        if luck > usuario:
            print(emojize('Errou!:disappointed: Tente novamente, porém com um número maior.', use_aliases=True))
        elif luck < usuario:
            print(emojize('Errou!:disappointed: Tente novamente, porém com um número menor.', use_aliases=True))
print(emojize(f'Parabéns! Com {tent} tentativa(s) vc ACERTOU :blush:', use_aliases=True))
print(f'>>> Vlw {nome[0]}, Até a próxima!')
sleep(1)
mixer.music.stop()