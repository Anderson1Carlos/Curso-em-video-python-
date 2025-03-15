preco = float(input('Informe o preço das contas: '))
print('FORMAS DE PAGAMENTO')
opcao = int(input(f'[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\nQual é a opção? '))

match opcao:
    case 1:
        print('Forma de pagamento selecionada: Dinheiro/Cheque --> 10% de desconto')
        print(f'Valor Bruto: R${preco:.2f}\nValor líquido: R${preco - (preco*(10/100))}')
    case 2:
        print('Forma de pagamento selecionada: Cartão --> 5% de desconto')
        print(f'Valor Bruto: R${preco:.2f}\nValor líquido: R${preco - (preco*(5/100))}')
    case 3:
        print('Forma de pagamento selecionada: Até 2x no cartão --> Preço formal')
        print(f'Valor Bruto: R${preco:.2f}\nValor líquido: R${preco:.2f}')
    case 4:
        parcelas = int(input('Informe a quantidade de parcela? '))
        print('Forma de pagamento selecionada: 3x ou mais no cartão --> 20% de juros')
        print(f'Sua compra será parcelada em {parcelas}x de R${preco / parcelas:.2f}')
        print(f'Valor Bruto: R${preco:.2f}\nValor líquido: R${preco + (preco*(20/100))}')
    case _:
        print('Opção inválida!')

