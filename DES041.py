# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: Mirim; Até 14 anos: infantil; Até 19 anos: junior; Até 20 ano: Sênior; Acima: Master
from datetime import date
atleta = input('Informe o nome do atleta: ').strip().capitalize()
nasc = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - nasc
if idade <= 9:
    print(f'O atleta (a) {atleta[0:atleta.find(" ")]} pertence a categoria MIRIM.')
elif idade <= 14:
    print(f'O atleta(a) {atleta[0:atleta.find(" ")]} pertence a categoria INFANTIL.')
elif idade <= 19:
    print(f'O atleta(a) {atleta[0:atleta.find(" ")]} pertence a categoria JUNIOR.')
elif idade <= 20:
    print(f'O atleta(a) {atleta[0:atleta.find(" ")]} pertence a categoria SÊNIOR.')
elif idade > 20:
    print(f'O atleta(a) {atleta[0:atleta.find(" ")]} pertence a categoria MASTER.')
else:
    print('Algo de errado nas informações fornecidas. Tente novamente.')