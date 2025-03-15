from datetime import date

ano_nasc = int(input('Informe a data de nascimento do atleta: '))

categoria = date.today().year - ano_nasc

if categoria <= 9:
    print(f'O atleta tem {date.today().year - ano_nasc} anos. Portanto, pertence a categoria MIRIM.')
elif categoria > 9 and categoria <= 14:
    print(f'O atleta tem {date.today().year - ano_nasc} anos. Portanto, pertence a categoria INFANTIL.')        
elif categoria > 14 and categoria <= 19:
    print(f'O atleta tem {date.today().year - ano_nasc} anos. Portanto, pertence a categoria JÚNIOR.')
elif categoria > 19 and categoria <= 25:
    print(f'O atleta tem {date.today().year - ano_nasc} anos. Portanto, pertence a categora SÊNIOR.')
elif categoria > 25:
    print(f'O atleta tem {date.today().year - ano_nasc} anos. Portanto, pertence a categora MASTER.')

