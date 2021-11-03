# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu e perdeu.
from random import randint
from emoji import emojize
from time import sleep
import pygame
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/happy-sandbox.wav')
pygame.mixer.music.play(loops=-1)
adorno = emojize(':boom:JOGO DA ADIVINHAÇÃO:boom:', use_aliases=True)
print(adorno)
luck = randint(0,5)
nome = input('>>> Qual seu nome? ').strip()
usuario = int(input(f'Ok! {nome[0:nome.find(" ")]}, de 0 a 5, tente adivinhar:  '))
print(emojize(':hourglass: Processando...', use_aliases=True))
sleep(2)
if usuario == luck:
    print(emojize('Parabéns! Acertou:blush:', use_aliases=True))
else:
    print(emojize('Errou!:disappointed:', use_aliases=True))
print(f'>>> Vlw {nome[0:nome.find(" ")]}, Até a próxima!')
sleep(1)
pygame.mixer.music.stop()



