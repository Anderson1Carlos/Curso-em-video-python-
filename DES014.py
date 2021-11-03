# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
adorno = ' FIM '
print("*"*38)
print(' CONVERSÃO DE CELSIUS PARA FAHRENHEIT ')
print('*'*38)
temp = float(input("Forneça a temperatura em Celcius: "))
print(f'{temp} ºC = {temp*1.8+32}ºF')
print(f'{adorno:-^38}')
