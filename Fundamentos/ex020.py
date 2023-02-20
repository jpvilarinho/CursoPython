# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

p1 = str(input('Primeira pessoa: '))
p2 = str(input('Segunda pessoa: '))
p3 = str(input('Terceira pessoa: '))
p4 = str(input('Quarta pessoa: '))
lista = [p1, p2, p3, p4]
random.shuffle(lista)
print('A ordem sorteada é igual a: {}'.format(lista))
