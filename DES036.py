# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))
teto = sal*(30/100)
mensal = anos*12
if casa/mensal > teto:
    print(f'\033[31mNegado\033[m. Valor da mensalidade: R${casa/mensal:.2f}. O valor do empréstimo necessário ultrapassa 30% do seu salário.')
elif casa/mensal < teto:
    print(f'\033[32mConcedido\033[m. Valor da mensalidade: R${casa/mensal:.2f}. Empréstimo de R${casa:.2f} será debitado em sua conta.')
