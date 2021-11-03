# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo; Qual é o nome ddo homem mais velho; Quantas mulheres tem menos de 20 anos.
media_idade = 0
velho = 0
nome_velho = ''
novinhas = 0
for c in range(1 ,5):
    nome = input('Informe o nome: ').capitalize().strip()
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo (feminino ou masculino): ').lower().strip()
    media_idade += idade
    if idade > velho and 'masculino' in sexo:
        velho = idade
        nome_velho = nome
    if 'feminino' in sexo:
        if idade < 20:
            novinhas += 1
print(f'Média de idade do grupo: {media_idade/4:.1f}\n'
      f'Nome do integrante masculino mais velho: {nome_velho}\n'
      f'Total de integrantes femininas com menos de 20 anos: {novinhas}')
