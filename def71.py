#Enfeites
print('='*30)
print(f'{'BANCO CEV':^30}')
print('='*30)

#Variáveis
cedulas, contadora = [50, 20, 10, 1], 0

#Eu sou um gêniokkkk
valor_saque = float(input('Que valor você quer sacar? R$'))
while True:
    cedula = valor_saque // cedulas[contadora]
    resto = valor_saque % cedulas[contadora]
    if valor_saque >= cedulas[contadora]:
        print(f'Total de {cedula:.0f} cédulas de R${cedulas[contadora]}')
        valor_saque = resto
    if resto == 0:
        break   
    contadora += 1
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
   