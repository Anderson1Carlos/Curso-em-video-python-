from datetime import date

#Captação dos dados de entrada que serão processados
ano_nasc = int(input('Informe seu ano de nascimento: '))

#Abaixo, duas variáveis que optei por usar pois assim os if/elif ficam menores, sei que gasta mais memória porém é um programa pequeno. 
ano_atual = int(str(date.today())[0:4]) # Aqui eu poderia ter usado date.today().year mas gostei da minha 'gambiarra' kkk.
idade = ano_atual - ano_nasc

#Estrutura de condição que definirá qual vai ser a saída dos dados. 
if idade > 18:
    print(f'Você tem {idade} anos. Soldado! Você está atrasado em {idade - 18} anos. Seu alistamento foi em {ano_nasc + 18}.')
elif idade < 18:
    print(f'Você possui {idade} anos, ainda falta {18 - idade} anos, aguarde seu momento até {ano_atual + (18 - idade)}.') 
elif idade == 18:
    print('Você possui 18 anos. Compareça a junta militar mais próxima e aliste- se já. Exército Braço forte, Mão amiga.') 
       

