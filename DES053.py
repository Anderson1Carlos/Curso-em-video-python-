# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''frase = input('Informe uma frase: ').strip().lower().split()
newfrase = ''.join(frase)
acc = ''
for c in range(len(newfrase)-1,-1,-1):
    acc += newfrase[c]
if acc == newfrase:
    print(f'O reverso de {" ".join(frase).capitalize()} é {acc}, portanto, é uma frase palíndroma.')
else:
    print(f'O reverso de {" ".join(frase).capitalize()} é {acc}, portanto, não é uma frase palíndroma.')'''
frase = 'Hoje eu estou bem'.split()
print(len(frase))


