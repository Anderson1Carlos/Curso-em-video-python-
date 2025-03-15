from math import sqrt
print(f'{' Cálculo da Hipotenusa ':-^41}')
cat_op = float(input('Informe o comprimento do cateto oposto: '))
cat_ad = float(input('Informe o comprimento do cateto adjacente: '))
print(f'Cateto oposto: {cat_op} \nCateto adjacente: {cat_ad} \nHipotenusa: {sqrt(cat_op * cat_op + cat_ad * cat_ad):.1f}')
print(f'{' FIM ':-^41}')





