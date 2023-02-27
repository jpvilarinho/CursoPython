# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from time import sleep
from random import randint

print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
sleep(1)

palpite_comp = randint(0, 10)
acertou = False
tentativas = 0

while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    tentativas += 1
    if palpite == palpite_comp:
        acertou = True
    else:
        if palpite < palpite_comp:
            print('Mais, tente novamente!')
            sleep(1)
        elif palpite > palpite_comp:
            print('Menos, tente novamente!')
            sleep(1)
print('Parabéns, você acertou após {} tentativa(s)'.format(tentativas))
