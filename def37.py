print('- Conversor de Bases Numéricas -')

#Captação de dados
num = int(input('Informe um número: '))
base = int(input('Selecione a base: \n[1] binário\n[2] Octal\n[3] Hexadecimal\n>>> '))

#Aqui eu poderia usar o if/elif/else mas optei por usa o switch case 
match base:
    case 1:
        print(f'Decimal: {num}\nBinário: {bin(num)[2:]}')
        #Essa funções de conversão -- bin, octal etc -- retornão um valor em str, logo da pra usar tecnicas de fateamento.
    case 2:
        print(f'Decimal: {num}\nOctal: {oct(num)[2:]}')
    case 3:
        print(f'Decimal: {num}\nHexadecimal: {hex(num)[2:]}')
    case _:
        print('Número Inválido')

    
