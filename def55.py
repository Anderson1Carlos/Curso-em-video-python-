max_peso = 0
min_peso = 0

for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        min_peso = peso
        max_peso = peso
    elif peso > max_peso:
        max_peso = peso
    elif peso < min_peso:
        min_peso = peso

print(f'O maior peso lido foi de {max_peso:.1f}kg')
print(f'O menor peso lido foi de {min_peso:.1f}kg')
