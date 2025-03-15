contadora = soma = maior = menor = 0


num = int(input('Digite um número: '))
contadora += 1
soma += num
maior = menor = num

quest = input('Quer continuar [S/N]: ').upper().strip()


if quest[0] not in 'SsNn':
    while quest not in 'SsNn':
        quest = input('Entrada inválida. Digite sua resposta novamente: ').upper().strip()
elif quest[0] in 'Ss':
    while quest[0] not in 'Nn':
        num = int(input('Digite um número: '))
        contadora += 1
        soma += num
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        quest = input('Quer continuar [S/N]: ').upper().strip()
print(f'''Você digitou {contadora} e a média foi {soma / contadora}.
O maior número foi {maior} enquanto o menor foi {menor}.
      ''')


