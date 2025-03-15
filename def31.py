distancia = int(input("Quantos Km's foram percorridos? "))
if distancia  <= 200:
    print(f'Preço da passagem: R${distancia *  0.50:.2f}')
else:
    print(f'Preço da passagem: R${distancia * 0.45:.2f}')


          

