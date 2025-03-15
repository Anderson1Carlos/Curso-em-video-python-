acu = 0

print('-'*30)
print(f'{'LISTAGEM DE PREÇO':^30}')
print('-'*30)


produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
             'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)



while True:
    print(f'{produtos[acu]:.<20}R$ ', end='')
    acu += 1
    print(f'{produtos[acu]:>6.2f}')
    acu += 1
    if acu == len(produtos):
        break

print('-'*30)