# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totC = qtdP = prodB = cont = 0
barato = ' '
while True:
    nome_produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))
    cont += 1
    totC += preco
    if preco > 1000:
        qtdP += 1
    if cont == 1 or preco < prodB:
        prodB = preco
        barato = nome_produto
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O total da compra é igual a {totC}')
print(f'A quantidade de produtos acima de R$1000 é igual a {qtdP}')
print(f'O nome do produto mais barato é {barato}')
