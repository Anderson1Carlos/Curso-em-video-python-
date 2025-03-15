maior, menor, numeros = 0, 0, list()

for c in range(0, 5):
    numeros.append(int(input(f'Informe o valor para a posição {c}: ')))
    
    if c == 0:
        maior = menor = numeros[c]
    elif numeros[c] > maior:
        maior = numeros[c]
        
    elif numeros[c] < menor:
        menor = numeros[c]
        
    
print('-='*30)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, num_ma in enumerate(numeros):
    if maior == num_ma:
        print(f'{pos}... ', end = '')
print('')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos, num_me in enumerate(numeros):
    if menor == num_me:
        print(f'{pos}... ', end = '')                
            
                
            
        





