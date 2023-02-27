# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

items = ['Pedra', 'Papel', 'Tesoura']
esc_pc = randint(0, 2)
print('''Opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
esc_j = int(input('Qual a sua jogada? '))
print('O computador escolheu {}'.format(items[esc_pc]))
print('O jogador escolheu {}'.format(items[esc_j]))

if esc_pc == 0:
    if esc_j == 0:
        print('Empate, jogue de novo!')
    elif esc_j == 1:
        print('Jogador venceu!')
    elif esc_j == 2:
        print('O computador venceu')
    else:
        print('Jogada inválida!')
if esc_pc == 1:
    if esc_j == 1:
        print('Empate, jogue de novo!')
    elif esc_j == 0:
        print('Computador venceu!')
    elif esc_j == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida!')
if esc_pc == 2:
    if esc_j == 2:
        print('Empate, jogue de novo!')
    elif esc_j == 0:
        print('Jogador venceu!')
    elif esc_j == 1:
        print('Computador venceu!')
    else:
        print('Jogada inválida!')