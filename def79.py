numeros, aux, pos_n = list(), 0, 0
while True:
    numeros.append(int(input('Informe um valor: ')))
    
    #Mecanisno anti-duplicata
    if len(numeros) > 1 :
        for pos, numero in enumerate(numeros):
            if numeros[aux] == numero and pos != pos_n:
                print('Valor duplicado! Não vou adicionar...')
                del numeros[aux] #Erro aqui
            else:
                print('Valor adcionado com sucesso!')

    
    
    resp = input('Quer continuar? [S/N]').strip().upper()
    if resp not in 'SN':
        while resp not in 'SN':        
            resp = input(('Opção inválida! Quer continuar [S/N] ')).upper().strip()
    else:
        if resp in 'N':
            break
    aux += 1
    pos_n += 1
print('-='*30)
print(f'Você digitou os valores {numeros}')

            
                
            
        





