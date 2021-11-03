# Faça um programa que leia a largura e a de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
altu = float(input('Informe a altura: '))
larg = float(input('Informe a largura: '))
print(f'Uma área de {altu*larg} m², equivale a {(altu*larg)/2:.1f}l de tinta.')