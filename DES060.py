# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1 = 120
num = int(input('Forneça um número: '))
result = num
const = num
while num != 0:
    if num == const:
        print(f'{num}!', end=' = ')
        print(f'{num}', end=' x ')
    elif num != 1:
        print(f'{num}', end=' x ')
    elif num == 1:
        print(f'{num}', end=' = ')
    num -= 1
    if num != 0:
        result *= num
if const == 0:
    print(f'{num}! = 1')
elif const != 0:
    print(result)
