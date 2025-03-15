from time import sleep

opcao = 0

print('Menu de opções')
valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))

while opcao != 5:
    print('''
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa
        ''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    print(' ')


    match opcao:
        case 1:
            print(f'A soma entre {valor_1} + {valor_2} é {valor_1 + valor_2}')
            
        case 2:
            print(f'O produto entre {valor_1} x {valor_2} é {valor_1 + valor_2}')
           
        case 3: 
            if valor_1 > valor_2:
                print(f'Entre {valor_1} e {valor_2} o maior valor é {valor_1}')
            
            elif valor_1 < valor_2:
                print(f'Entre {valor_1} e {valor_2} o maior valor é {valor_2}')
       
            else:
                print(f'Números idênticos!')
                
        case 4:
            valor_1 = int(input('Primeiro valor: '))
            valor_2 = int(input('Segundo valor: '))
            
        case 5:
            print('Saindo do programa...')
            sleep(1)
        case _:
            print('Entrada inválida!')
            
        






    