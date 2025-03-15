palavras = ('aprender', 'programar', 'linguagem', 
'python', 'curso', 'gratis', 'estudar', 'praticar', 
'trabalhar', 'mercado', 'programador', 'futuro')

vogais = ('a', 'e', 'i', 'o', 'u')

for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c].upper()} temos ', end='') 
    for d in range(0, len(palavras[c])):
        for vogal in vogais:
            if vogal == palavras[c][d]:
                print(vogal, end=' ')
    print(' ')

    

                
            
                
            
        





