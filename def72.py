#Bibliotecas - Usei pq acho elas úteis, portanto não quero esquece-las. Mas nesse programa estão mais pra enfeite mesmo.
from os import system
from time import sleep

#Tupla
contagem = ('zero', 'um', 'dois', 'três', 'quatro',
             'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'quartoze',
                 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                   'dezenove', 'vinte')
#Entrada com estrutura de repetição caso o animal do usuário erre o número
while True:
    num = int(input('Entre 0 a 20, informe um número: '))
    if num <= 20 and num >= 0:
        break
    print('Entrada inválida!')
    sleep(1)
    system('cls')


print(contagem[num])