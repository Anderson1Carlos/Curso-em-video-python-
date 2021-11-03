# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
cata = float(input('Informe o cateto adjacente: '))
cato = float(input('Informe o cateto oposto: '))
print(f'Hipotenusa: {hypot(cato,cata):.2f}')
