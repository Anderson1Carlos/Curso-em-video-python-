# Crie um program que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, O nome com todas minúsculas, quantos letras ao todo (sem considerar espaços), quantas letras tem o primeiro nome.
from time import sleep
from emoji import emojize
from os import system
import pygame
adorno = ' YOURNAME '
print(f'{adorno:-^32}')
nome = str(input('Digite seu nome completo: ')).strip()
print(emojize('Ok:thumbs_up:'))  # Ñ coloquei o use_aliases=True pois ñ mudou porra nenhuma ao meu ver.
sleep(2)
system('cls')  # Esse comando para limpar não funciona no pycharm além de da um erro de caractere.
newname = nome.split()
junto = ''.join(newname)
print(f'Seu nome com todas as letras maiúscula: {nome.upper()} \nSeu nome com todas as letras minúscula: {nome.lower()} \nQuantidade de letras do nome: {len(junto)}\nQuantas letras tem seu primerio nome: {nome.find(" ")}')
print(emojize('GOOD BYE:wave:', use_aliases=True))  # Já aqui foi preciso senão ñ funfa.
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/good bye_female.wav')
pygame.mixer.music.play()
sleep(3)
pygame.mixer.music.stop()

#  Na quantidade de letras do nome total, eu poderia subitrair o len - count''