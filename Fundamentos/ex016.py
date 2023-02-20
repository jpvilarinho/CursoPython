# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

num = float(input('Digite um número qualquer: '))
print('O numero {} possui como parte inteira: {}'.format(num, math.trunc(num)))
