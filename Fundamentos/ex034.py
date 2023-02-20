# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual é o salário do funcionário? R$'))

if sal > 1250:
    aum = sal * 0.1
    nsal = sal + aum
    print('Com o aumento do salário de R${:.2f}, o salário final fica igual a R${:.2f}'.format(aum, nsal))
if sal <= 1250:
    aum = sal * 0.15
    nsal = sal + aum
    print('Com o aumento do salário de R${:.2f}, o salário final fica igual a R${:.2f}'.format(aum, nsal))
else:
    print('Aconteceu um erro, você digitou no formato correto?')
