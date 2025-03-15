lado1 = float(input('Informe o tamanho do lado 1: '))
lado2 = float(input('Informe o tamanho do lado 2: '))
lado3 = float(input('Informe o tamanho do lado 3: '))

if (lado1 + lado2) >  lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    if lado1 == lado2 == lado3:
        print('Forma um triângulo Equilátero!')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('Forma um triângulo Isósceles!')
    elif lado1 != lado2 != lado3:
        print('Forma um triângulo Escaleno!')    
else: 
    print('Dada a condição de existência, onde cada lado deve ser menor que a soma dos outros dois, não forma triângulo.')    
    