# Crie um programa que faça o computador jogar jokenpô com você.
from random import choice
usuario = input('JO, KEN, PO: ').lower().strip()
elementos = ['pedra', 'papel', 'tesoura']
cpu = choice(elementos)
if cpu == 'pedra' and usuario == 'tesoura' or cpu == 'tesoura' and usuario == 'papel' or cpu == 'papel' and usuario == 'pedra':
    print(f'Máquina: {cpu.capitalize()}\nUsuário: {usuario.capitalize()}\nCPU WINS!!!')
elif usuario == 'pedra' and cpu == 'tesoura' or usuario == 'tesoura' and cpu == 'papel' or usuario == 'papel' and cpu == 'pedra':
    print(f'Usuário: {usuario.capitalize()}\nCPU: {cpu.capitalize()}\nParabéns!!!')
elif usuario == cpu:
    print(f'Empate! Ambos forneçeram o mesmo valor: {cpu}')
else:
    print('Algo deu errado. Repita os procedimentos.')

