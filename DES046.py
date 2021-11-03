# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
from pygame import mixer
from emoji import emojize
mixer.init()
mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/fireworks.wav')
for c in range(10,0,-1):
    print(c)
    sleep(3)
mixer.music.play()
print(emojize(f':fireworks:{"Feliz ano novo":_^20}:fireworks:', use_aliases=True))
sleep(10)
mixer.music.stop()
