# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar, Se é a hora de se alistar, Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
from emoji import emojize
nasc = int(input('Informe sua data de nascimento: '))
idade = date.today().year - nasc
if idade < 18:
    print(f'Sua hora ainda não chegou! Ainda faltam {18 - idade} anos')
elif idade == 18:
    print(emojize('Está na hora combatente. Sua nova namorada agora se chama fal762. Parabéns :skull:', use_aliases= True))
else:
    print(emojize('Já passou da hora de você se alistar né BISONHO?!!! Se já se alistou paga 20 aê então. :muscle:', use_aliases= True))