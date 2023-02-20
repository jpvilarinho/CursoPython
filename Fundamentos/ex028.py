# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

num_computador = randint(0, 5)
print('-*-' * 18)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')  # Faz o computador "PENSAR"
print('-*-' * 18)
num_jogador = int(input('Em que número eu pensei: '))  # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)

if num_jogador == num_computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('Ganhei, eu pensei no número {} e não no número {}'.format(num_computador, num_jogador))
