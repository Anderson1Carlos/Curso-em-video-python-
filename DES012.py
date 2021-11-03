# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
adorno = ' Descontador de descontos '
adorno1 = ' Fim '
print(f'{adorno:=^32}')
preco = float(input('Digite o preço:R$ '))
vdesc = int(input('Digite o desconto (%): '))
desc = preco*(vdesc/100)
print(f'Preço pós-desconto de : R$ {preco-desc:.2f}')
print(f'{adorno1:=^32}')

