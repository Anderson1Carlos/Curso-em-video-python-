# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
adorno = 'Antecessor&Sucessor'
print(f'{adorno:-^35}')
num = int(input('Informe um número: '))
print(f'Antecessor: {num-1}\nAtual: {num}\nSucessor: {num+1}')
adornofinal = 'Fim'
print(f'{adornofinal:-^35}')
