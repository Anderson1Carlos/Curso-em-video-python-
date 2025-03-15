print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

termos = int(input('Quantos termos vc quer mostrar? '))

contadora = 0
a = 0
b = 1
c = a + b

while termos != contadora:
    if termos == 1:
        print(f'{a} --> ', end='')
        contadora += 1
    elif termos == 2:
        print(f'{a} --> ', end='')
        a = b
        b = c
        c = a + b
        contadora += 1
    elif termos >= 3:
        print(f'{a} --> ', end='')
        a = b
        b = c
        c = a + b
        contadora += 1

print('FIM')

    
