nome = input('Digite seu nome completo: ').strip()
print(f'Maiúsculo: {nome.upper()} \nMinúsculo: {nome.lower()} \nQuantas letras: {len(nome) - nome.count(' ')} \nPrimeiro nome: {nome[0:nome.find(' ')]} possui {len(nome[0:nome.find(' ')])} letras.')

