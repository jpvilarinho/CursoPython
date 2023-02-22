# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

p = float(input('Digite seu peso(kg): '))
a = float(input('Digite sua altura(m): '))
imc = (p / (a ** 2))

if imc < 18.5:
    print('IMC igual a {:.2f} e o status é abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC igual a {:.2f} e o status está no peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('IMC igual a {:.2f} e o status está em sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print('IMC igual a {:.2f} e o status está em obesidade'.format(imc))
else:
    print('IMC igual a {:.2f} e o status está em obesidade mórbida'.format(imc))
