media_idade = 0
maiordas_idades = 0
mais_velho = ''
acumulativa = 0

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ').upper().strip()
    media_idade += idade
    if sexo[0] == 'M':
        if idade > maiordas_idades:
            maiordas_idades = idade
            mais_velho = nome
    elif sexo[0] == 'F':
        if idade < 20:
            acumulativa += 1


print(f'A média de idade do grupo é de {media_idade / 4:.1f} anos.')
print(f'O homem mais velho tem {maiordas_idades} e se chama {mais_velho}.')
print(f'Ao todo são {acumulativa} mulheres com menos de 20 anos.')

