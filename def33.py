# Questionário
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

# Estrurura de condição que definirá qual é o valor maior e, por consequente, o valor médio e o menor.
if numero1 == numero2 and numero2 == numero3: # Aqui, o objetivo é tirar a hipótese de que o usuário digite o todos os números iguais.
    print('Todos os números são iguais')
else:
    # Escopo 1 (Número 1 sendo o maior)
    if numero1 >= numero2 and numero2 >= numero3:
        print(f'Maior: {numero1}\nMédio: {numero2}\nMenor: {numero3}')
        
    elif numero1 > numero3 and numero3 > numero2:
        print(f'Maior:{numero1} \nMédio: {numero3}\nMenor: {numero2} ')
        
    # Escopo 2 (Número 2 sendo o maior)
    elif numero2 > numero1 and numero1 >= numero3:
        print(f'Maior: {numero2}\nMédio: {numero1}\nMenor: {numero3}')

    elif numero2 > numero3 and numero3 > numero1:
        print(f'Maior: {numero2}\nMédio: {numero3}\nMenor: {numero1}')
    
    # Escopo 3 (Número 3 sendo o maior)
    elif numero3 >= numero2 and numero2 >= numero1:
        print(f'Maior: {numero3}\nMédio: {numero2}\nMenor: {numero1}')
    
    elif numero3 > numero2 and numero1 > numero2:
        print(f'Maior: {numero3}\nMédio: {numero1}\nMenor: {numero2}')
        
     
