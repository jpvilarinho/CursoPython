# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date

totmaior = 0
totmenor = 0

for p in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E {} pessoas menores de idade'.format(totmenor))

