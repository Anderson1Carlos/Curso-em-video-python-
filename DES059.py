# Crie um programa que leia dois valores e mostre um menu na tela: [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
chave = False
operacao = 0
op_um = int(input('Informe o primeiro operando: '))
op_dois = int(input('Informe o segundo operando: '))
while operacao != 5:
    operacao = int(input('Escolha a operação:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n--> '))
    if operacao == 1:
        print(f' {op_um} + {op_dois} = {op_um + op_dois}')
    elif operacao == 2:
        print(f'{op_um} x {op_dois} = {op_um * op_dois}')
    elif operacao == 3:
        if op_um > op_dois:
            print(f'{op_um}')
        elif op_dois > op_um:
            print(f'{op_dois}')
    elif operacao == 4:
        op_um = int(input('Informe o primeiro operando: '))
        op_dois = int(input('Informe o segundo operando: '))
    else:
        print('Fez merda né?! Tenta dnovo.')
        operacao == 0
    print('-'*30)
print('Até a próxima!')