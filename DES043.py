# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, e calcule seu  IMC e mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5: Abaixo do peso; Entre 18.5 e 25: Peso ideal; 25 até 30: sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade mórbida.
adorno = ' IMC '
print('\033[32m-\033[m'*20)
print(f'\033[34m{adorno:-^19}\033[m')
print('\033[32m-\033[m'*20)
peso = int(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Vai comer graveto! Vc está abaixo do peso: {imc:.1f}')
elif 18.5 <= imc < 25:
    print(f'Parabéns! Vc está no seu peso ideal: {imc:.1f}')
elif 25 <= imc < 30:
    print(f'Cuidado! Tá ficando pançudinho(a). Vc está no sobrepeso {imc:.1f}')
elif 30 <= imc < 40:
    print(f'Fecha a boquinha aêo Barril destampado kkkkkkjj. Tá obeso: {imc:.1f}')
elif imc >= 40:
    print(f'\033[31;7mVc está com obesidade mórbida:\033[m {imc:.1f}. \033[4;34mProcure ajuda médica!\033[m')
else:
    print('Algo de errado aconteceu! Tente novamente.')