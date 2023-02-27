# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o salário do funcionário: R$'))
aum = s * 0.15
ns = s + aum
print('O salário do funcionário R${:.2f}, com aumento de 15% é igual a R${:.2f}'.format(s, ns))
