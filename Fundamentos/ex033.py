# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o primeiro valor: '))
n3 = int(input('Digite o primeiro valor: '))

menor = n1

if n1 > n2 and n3 > n2:
    menor = n2
if n1 > n3 and n2 > n3:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if menor == maior:
    print('Os 3 valores são iguais.')
else:
    print('O menor valor digitado é igual a {}'.format(menor))
    print('O maior valor digitado é igual a {}'.format(maior))


