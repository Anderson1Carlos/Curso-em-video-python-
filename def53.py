frase = input('Digite uma frase: ').upper().strip().split()
frase2 = "".join(frase)

pont_b = len(frase2) - 1
aux = 0

print(f'O inverso de {frase2} é ', end='')
for c in range(len(frase2) - 1, -1, -1):
    print(frase2[c], end='')
    if frase2[c] == frase2[pont_b]:
        aux += 1
    pont_b -= 1

print('')

if len(frase2)  == aux:
    print('A frase digitada é PALÍNDROMO!')
else:
    print('A Frase digitada não é PALÍNDROMO!')


  
