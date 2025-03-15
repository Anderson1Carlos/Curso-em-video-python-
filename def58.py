from random import randint

contadora = 1

cpu = randint(0,10)

usuario = int(input('Tente adivinhar entre um núemro de 0 a 10: '))

while cpu != usuario:
    if cpu > usuario:
        print('Mais... Tente mais uma vez!')
        contadora += 1
        usuario = int(input('Qual o seu palpite? '))
    else:
        print('Menos... Tente mais uma vez!')
        contadora += 1
        usuario = int(input('Qual o seu palpite? '))

print(f'Acertou com {contadora} tentativas. Parabéns!')


    






    