frase = input('Digite uma frase: ').upper().strip()
print(f'Qtd. de aparições do "A": {frase.count('A')}\nPrimeira vez que ele aparece: {frase.find('A')}\nUltima ocorrência: {frase.rfind('A')}')
