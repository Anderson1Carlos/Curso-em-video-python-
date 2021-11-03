# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra 'A', Em que posição ela aparece a primeira vez, em que posição ela aparece a última vez.
import pygame
from time import sleep
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/bassloops.wav')
pygame.mixer.music.play(loops=-1)
adorno = ' Analisador de frases '
print(f'{adorno:-^33}')
frase = input('Digite uma frase: ').upper().strip()
par = len(frase)
print(f'Quantidade de letra a: {frase.count("A")}\nPrimeira a aparição do a: {frase.find("A")+1}\nÚltima posisão do a: {frase.rfind("A")+1}')
sleep(1)
pygame.mixer.music.stop()

