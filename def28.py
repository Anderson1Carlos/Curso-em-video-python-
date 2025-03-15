from random import randint
cpu = randint(0,5)
usuario = int(input('Tente adivinhar: '))
print('Acertou!' if cpu == usuario else 'Perdeu!')
