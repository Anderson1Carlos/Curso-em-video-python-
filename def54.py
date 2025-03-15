from datetime import datetime

ano_atual = datetime.now().year
maiores = 0 
menores = 0


for c in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = ano_atual - ano_nasc
    if idade < 18:
        maiores += 1
    elif idade >= 18:
        menores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade.')
print(f'E também tivemos {menores} menores de idade.')
    

