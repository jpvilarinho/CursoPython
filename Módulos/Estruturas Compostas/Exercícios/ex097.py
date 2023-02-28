# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.

from time import sleep


def mostralinha():
    print('~'*12)


def escreva(msg):
    mostralinha()
    sleep(1)
    print(msg)
    sleep(1)
    mostralinha()


texto = str(input('Digite o texto a ser adaptado: '))
escreva(texto)
