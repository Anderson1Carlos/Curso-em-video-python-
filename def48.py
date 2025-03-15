
acumuladora = 0 
contadora = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        contadora += 1
        acumuladora += c
print(f'A soma de todos os {contadora} valores solicitados é {acumuladora}')

    
    

