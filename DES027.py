# Faça um program que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. ex: Ana maria de Souza. Primeiro: Ana Última: Souza.
import pygame
from time import sleep
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/bassloops.wav')
pygame.mixer.music.play(loops=-1)
adorno = ' Analisador de nomes '
print(f'{adorno:-^33}')
name = input('Digite seu nome: ').strip()
print(f'Primeiro nome: {name[0:name.find(" ")]}\nÚltimo nome: {name[name.rfind(" "):]}')
sleep(1)
pygame.mixer.music.stop()

