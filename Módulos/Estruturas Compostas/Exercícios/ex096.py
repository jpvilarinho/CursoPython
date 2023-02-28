# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno de {larg} x {comp} é igual a: {a}m²')


l = float(input('Digite a largura(m) do terreno: '))
c = float(input('Digite o comprimento(m) do terreno: '))
área(l, c)
