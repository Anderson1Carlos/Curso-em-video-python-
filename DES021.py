# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
import pygame
from time import sleep
pygame.mixer.init()  # Iniciar o mixer.
pygame.mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/musictest.wav')  # Carrega o audio
pygame.mixer.music.play(loops=-1)  # Da o play na música de maneira normal, loop, repetições ou de maneira infinita.
print('TUTS TUTS')
sleep(30)
pygame.mixer.music.stop()  # Para parar a música.
print('Acabou')
sleep(5)
'''
pygame.mixer.music.pause() --> Para pausar a música.
pygame.mixer.music.unpause() --> Despausar.
pygame.mixer.music.rewind() --> Reinicia a música. 
pygame.mixer.music.set_volume() --> Define o volume da música (os parâmetros são em float).
'''



