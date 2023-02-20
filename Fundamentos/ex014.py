# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite o valor da temperatura, em ºC: '))
f = (c * 1.8) + 32
print('A temperatura {}ºC, com a conversão fica igual a {}ºF'.format(c, f))
