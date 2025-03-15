while True:
    print('-'*30)
    print('''Operações --> 
          [1] Soma
          [2] Subtração
          [3] Multiplicação
          [4] Divisão
        ''')
    operacao = int(input('Informe a operação: '))
    valor = int(input('Informe o operador: '))
    print('='*30)
    
    while True:
        match operacao:
            case 1:
                print('-'*30)  
                for c in range(1, 11):
                    print(f'{valor:^2} + {c:^3} = {valor + c:^3}')
                print('-'*30)
            case 2:
                print('-'*30)
                for c in range(1,11):
                    print(f'{valor:^2} - {c:^3} = {abs(valor - c):^3}')
                print('-'*30)
            case 3:
                print('-'*30)
                for c in range(1, 11):
                    print(f'{valor:^2} x {c:^3} = {valor * c:^3}')
                print('-'*30)
            case 4:
                print('-'*30)
                for c in range(1, 11):
                    print(f'{valor:^2} : {c:^3} = {valor / c:.1f}')
                print('-'*30)
            case _:
                    print('-'*30)
                    print('Operação invélida!') 
                    print('-'*30)

        resp = input('Deseja continuar? [S/N] ').strip().upper()
        if resp[0] in 'Nn':
            break
        elif resp[0] in 'Ss':
            resp2 = (input('Deseja trocar a operação? [S/N] ')).strip().upper()
            if resp2[0] in 'Ss':
                print('-'*30)
                print('''Operações --> 
                        [1] Soma
                        [2] Subtração
                        [3] Multiplicação
                        [4] Divisão
                        ''')
                operacao = int(input('Informe a operação: '))
            resp3 = (input('Quer mudar o operador? [S/N] ')).strip().upper()
            if resp3[0] in 'Ss':
                valor = int(input('Informe o operador: '))
                


    break




   