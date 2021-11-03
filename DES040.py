# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atinginda: média abaixo de 5.0; Média entre 5.0 e 6.9: recuperação; Média 7.0 ou superior: aprovado.
from time import sleep
from pygame import mixer
from emoji import emojize

tiltle = 'BOLETIM FINAL'
print('=' * 20)
print(f'{tiltle:-^20}')
print('=' * 20)
nome = input('Informe seu nome completo? ').strip().capitalize()
nota = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
print('Processando notas...')
media = (nota + nota2) / 2
sleep(2)
mixer.init()
if media < 5:
    mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/scream-noooh.wav')
    mixer.music.play()
    print(f'Olá {nome[0:nome.find(" ")]}, sua média foi de {media}, portanto você perdeu.')
    sleep(5)
    mixer.music.stop()
elif 5 <= media <= 6.9:
    mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/suspense.mp3')
    print(f'Olá {nome[0:nome.find(" ")]} sua média foi de {media}, portanto você está na recuperação. Se prepare!')
    mixer.music.play()
    print(emojize('Será que vai passar? :eyes:', use_aliases=True))
    sleep(10)
    mixer.music.stop()
elif media >= 7:
    mixer.music.load('C:/Users/Anderson/PycharmProjects/engateando/GTA SA win.mp3')
    print(emojize(f'Parabéns! {nome[0:nome.find(" ")]} sua média foi {media}, portanto você passou. :clap:', use_aliases=True))
    mixer.music.play()
    sleep(8)
    mixer.music.stop()
else:
    print('Algo de errado aconteceu, repita o procedimento do começo!')

