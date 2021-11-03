# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: Á vista dinheiro/cheque: 10% de desconto; Á vista no cartão: 5% de desconto; Em até 2x no cartão: preço normal: 3x ou mais no cartão: 20% de juros
preco = float(input('Qual o valor da conta? '))
alt = int(input('Pressione [1] para pagamento á vista: dinheiro/cheque.\nPressione [2] para pagamento á vista: cartão.\nPressione [3] para pagamento parcelado: 2x\nPressione [4] para pagamento parcelado: 3x ou mais.\n>>> '))
if alt == 1:
    print(f'Preço original: R${preco:.2f}\nPreço com desconto (10%): R${abs(preco*(10/100)-preco):.2f}')
elif alt == 2:
    print(f'Preço original: R${preco:.2f}\n Preço com desconto (5%): R${abs(preco*(5/100)-preco):.2f}')
elif alt == 3:
    print(f'Preço original: R${preco:.2f}\nValor parcelado (2x): R${preco/2:.2f}\n\033[31m*Esta opção de pagamento não contém descontos/juros\033[m.')
elif alt == 4:
    par = int(input('Quantas parcelas? - de 3 a 12x. >>> '))
    print(f'Preço original: R${preco:.2f}\nPreço com juros (20%): R${abs(preco*(20/100)+preco):.2f}\nValor parcelado ({par}x): R${abs((preco*(20/100)+preco)/par):.2f} ')
else:
    print('Algo de errado ocorreu. Como usuário burro que és, deve ter feito merda pra variar.')