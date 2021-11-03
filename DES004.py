# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
algo = input('Digite qualquer coisa: ')
print(f'Tipo da variável: {type(algo)}\nSomente número? {algo.isnumeric()}\nSomente letra? {algo.isalpha()}\nLetra '
      f'e/ou número? {algo.isalnum()}\nEstá em letra maiúscula? {algo.isupper()}\nEstá em letra minús'
      f'cula? {algo.islower()}\nSó contém espaços? {algo.isspace()}')





