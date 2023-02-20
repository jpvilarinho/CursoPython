# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Digite a largura da parede(m): '))
h = float(input('Digite a altura da parede(m): '))
a = l * h
t = a / 2
print('A parede possui dimensões de {} de largura e {} de altura. Assim sua área será igual a {:.2f}m²'.format(l, h, a))
print('Para pintar a parede com uma área de {:.2f}m², serão necessários {:.2f} litros de tinta.'.format(a, t))
