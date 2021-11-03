# Refaça o des035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero: todos os lados iguais; Isósceles: Dois lados iguais; Escaleno: Todos os lados diferentes.
reta1 = float(input('Informe a primeira reta: '))
reta2 = float(input('Informe a segunda reta: '))
reta3 = float(input('Informe a terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3 + reta2 > reta1:
    if reta1 == reta2 == reta3:
        print('Condições favoráveis para formar um triângulo Equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Condições favoráveis para formar um triângulo Isósceles.')
    else:
        print('Condições favoráveis para formar um triângulo Escaleno.')
else:
    print('Condições inaptas para formar um triângulo.')