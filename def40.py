
print('- Média Aritimética -')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média foi {media:.1f}. Você perdeu!')
elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media:.1f}. Recuperação!')
elif media >= 7:
    print(f'Sua média foi {media:.1f}. Parabéns! Aprovado(a)')    
