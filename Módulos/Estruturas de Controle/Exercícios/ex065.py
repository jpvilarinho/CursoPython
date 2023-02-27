# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

r = 'S'
s = qtd = med = max = min = 0

while r in 'Ss':
    num = int(input('Digite um valor inteiro qualquer: '))
    s += num
    qtd += 1
    if qtd == 1:
        max = min = num
    else:
        if num > max:
            max = num
        if num < min:
            min = num
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
med = s / qtd
print('\nVocê digitou {} número(s) e a média dele(s) é igual a {}'.format(qtd, med))
print('O maior valor é igual a {} e o menor é igual a {}'.format(max, min))