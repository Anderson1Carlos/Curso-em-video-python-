# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
d = 'Dobro (x2)'
t = 'Triplo (x3)'
rq = 'Raiz quadrada (√)'
print(f'{d:°<24}\n{rq:-^23}\n{t:°>24}')
num = float(input('Digite um número: '))
# Em relação a obtenção da raiz quadrada, podemos realiza-lá das seguintes maneiras: Utilizando a função pow (potênciação, da biblioteca math) na qual elevamos o número a 0.5, ou utilizamos a função sqrt (radiciação, também da biblioteca math). A outra maneira foi esta utilizada.
print(f'Dobro: {num*2:.1f}\nTriplo: {num*3:.1f}\nRaiz quadrada: {num**(1/2):.1f}')




