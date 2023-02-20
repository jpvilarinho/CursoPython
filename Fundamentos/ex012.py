# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o valor do produto: R$'))
d = (p * 0.05)
np = p - d
print('O produto de valor inicial R${:.2f}, com desconto de 5%, fica com valor final igual a R${:.2f}'.format(p, np))
