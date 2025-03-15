num = 0
contadora = 0
acumuladora = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        contadora += 1
        acumuladora += num
print(f'Você digitou {contadora} números e a soma entre eles foi {acumuladora}.')


    
