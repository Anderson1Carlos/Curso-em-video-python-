# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe o sexo (M/F) : ')).upper()[0].strip()
while sexo not in 'FMfm':
    sexo = input('Dados incorretos. Informe o sexo (M/F): ').strip().upper()[0]
if sexo in 'Mm':
    print('Sexo masculino registrado com sucesso.')
elif sexo in 'Ff':
    print('Sexo feminino registrado com sucesso.')


