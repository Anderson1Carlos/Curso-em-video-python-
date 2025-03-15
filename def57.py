
sexo = input('Informe seu sexo [M/F]: ').upper().strip()
while sexo[0] not in 'MmFf':
        sexo = input('Dados inválidos. Por favor, informe seu sexo [M/F]: ').upper().strip()
match sexo:
        case 'M':
                print('Sexo Masculino registrado com sucesso!')
        case 'F':
                print('Sexo Feminino registrado com sucesso!')  

                



    