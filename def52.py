contadora = 0
num = int(input('Informe um número: '))
for c in range(1,num + 1):
    if num % c == 0:
        print(c,end=' ')
        contadora += 1
    else:
        print(c, end= ' ')
print(f'O número {num} foi divisível {contadora} vezes.')
if contadora > 2:
    print('E por isso não é primo!')
else:
    print('E por isso é primo!')
