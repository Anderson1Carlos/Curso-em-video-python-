nome = input('Digite seu nome completo: ').strip()
print('Muito prazer!')
print(f'Seu primeiro nome é {nome[:nome.find(' ')]}.\nSeu último nome é {nome[nome.rfind(' '):len(nome)]}.')
