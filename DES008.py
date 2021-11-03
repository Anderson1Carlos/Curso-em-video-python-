# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print('-'*32)
print('CONVERSÃO MEDIDAS DE COMPRIMENTO')
print('-'*32)
metro = float(input('Diga quantos metros: '))
print(f'Metro informado: {metro}\nEm quilômetros: {metro/1000}\nEm hectômetro: {metro/100}\nEm decâmetro: {metro/10}\nEm decímetro: {metro*10}\nEm centímetros: {metro*100:.0f}\nEm milímetros: {metro*1000:.0f}')
adorno = ' FIM '
print(f'{adorno:-^32}')



