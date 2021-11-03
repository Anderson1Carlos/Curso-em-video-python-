print('\033[41mteste\033[m')
print('\033[4;33;44mteste\033[m')
print('\033[1;35;43mteste\033[m')
print('\033[42mteste\033[m')
print('\033[7mteste\033[m')
print('\033[mteste\033[m')
cores = {'amarela':'\033[33m', 'azul':'\033[34m', 'limpa': '\033[m'}
nome = 'anderson'
print(f'Óla, {cores["amarela"]} {nome},{cores["limpa"]} {cores["azul"]} tudo bem?')
print(f'\033[31;44m {nome}')  # O código ansi ñ funciona dentro da máscara de substituição



