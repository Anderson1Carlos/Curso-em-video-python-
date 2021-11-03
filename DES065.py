# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual  foi o maior e o menor valores lidos. O programa deve  perguntar ao usuário se ele quer ou não continuar a digitar valores.
acu = 0
soma = 0
question = ' '
maior = 0
menor = 0
while question[0] not in 'Nn':
    num = int(input('Informe um número: '))
    soma += num
    acu += 1
    if num > maior:
        maior = num
    if acu == 1:
        menor = num
    elif num < menor:
        menor = num
    question = str(input('Pretende digitar mais valores? (Digite Sim ou Não): ')).strip().upper()[0]
print(f'A média final entre os valores foi de {soma / acu}. O menor número foi {menor} enquanto o maior foi {maior}.')

