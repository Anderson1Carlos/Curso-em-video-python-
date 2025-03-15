#Bibliotecas
from time import sleep
from os import system

#Variáveis
preco_final, mais_demil, barato_preco, barato_nome = 0, 0, 0, None


#Enfeites
print('-'*50)
print(f'{'LOJA SUPER BARATÃO':^50}')
print('-'*50)

#Uso do laço de repetição while
while True:
    #Entrada de dados
    nome_produto = input('Nome do produto: ').strip().upper()
    preco = float(input('Preço: R$'))
    print('-'*30)

    #Processamento para saída:   
    preco_final += preco #Valor final a ser pago

    if preco > 1000:
        mais_demil += 1 #Qtd. de produtos acima de R$1000

    if preco < barato_preco: #Preço e nome do produto mais barato
        barato_nome = nome_produto 
        barato_preco = preco

    elif barato_preco == 0: #Como a inicialização da variável começou com 0, é de consenso que a maioria dos produtos não são gratuitos, 
                            #então tive que criar esse artifício para de fato obter produto mais barato.  
        barato_nome = nome_produto
        barato_preco = preco
    
    #Validação da repetição do programa
    resposta = input('Quer continuar [S/N]: ').strip().upper()[0]
    while resposta[0] not in 'SsNn':
        resposta = input('Entrada inválida! Quer continuar? [S/N]: ').strip().upper()[0]
    #Botei o sleep só de enfeite e pra eu ñ me esquecer dessa função:)
    if resposta[0] in 'Nn':
        print('Ok, saindo...')
        sleep(1)
        break

    print('-='*15)
print(f'{' FIM DO PROGRAMA ':-^50}')
#Relatório final em um print só para não gerar muitas chamadas no SO(isso depois de eu enfeitar todo o código :b)
print(f'''
O total da compra foi R${preco_final:.2f}
Temos {mais_demil} produtos custando mais de R$1000.00
O produto mais barato foi {barato_nome} que custa R${barato_preco} 

''')