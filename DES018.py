# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
adorno = 'SENO, COSSENO E TANGENTE'
fim = ' FIM '
print(f'{adorno:¨^34}')
from math import cos, sin, tan, radians
ang = int(input('Informe o ângulo: '))
print(f'Seno: {sin(radians(ang)):.2f}\nCosseno: {cos(radians(ang)):.2f}\nTangente: {tan(radians(ang)):.2f}')
print(f'{fim:-^34}')
