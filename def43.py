print('- Índice de Massa Corporal (IMC) -')
peso = float(input('Informe seu peso: '))
altura = float(input('informe sua altura: '))
imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'Seu peso atual: {peso}\nSua altura atual: {altura:.2f}\nSeu IMC: {imc:.1f}\n\033[1;31mABAIXO DO PESO\033[m')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu peso atual: {peso}\nSua altura atual: {altura:.2f}\nSeu IMC: {imc:.1f}\n\033[0;32mPESO IDEAL\033[m')
elif imc >= 25 and imc <= 30:
    print(f'Seu peso atual: {peso}\nSua altura atual: {altura:.2f}\nSeu IMC: {imc:.1f}\n\033[0;33mSOBREPESO\033[m')
elif imc >= 30 and imc <= 40:
    print(f'Seu peso atual: {peso}\nSua altura atual: {altura:.2f}\nSeu IMC: {imc:.1f}\n\033[0;31mOBESIDADE\033[m')
elif imc > 40:
    print(f'Seu peso atual: {peso}\nSua altura atual: {altura:.2f}\nSeu IMC: {imc:.1f}\n\033[1;31mOBESIDADE MÓRBIDA\033[m')            


