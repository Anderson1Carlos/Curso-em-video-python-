lado1 = float(input('Informe o tamanho do lado 1: '))
lado2 = float(input('Informe o tamanho do lado 2: '))
lado3 = float(input('Informe o tamanho do lado 3: '))
# Escopo 1 
if (lado1 + lado2) >  lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    print('Forma triângulo!')
else: 
    print('Dada a condição de existência, onde cada lado deve ser menor que a soma dos outros dois, não forma triângulo.')    
    