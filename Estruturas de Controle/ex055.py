# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []

for p in range(1, 6):
    peso = float(input('Qual o peso da {}ª em kg? '.format(p)))
    lista += [peso]
print('\nO maior peso registrado foi o de {}Kg e o menor foi o de {}Kg'.format(max(lista), min(lista)))
