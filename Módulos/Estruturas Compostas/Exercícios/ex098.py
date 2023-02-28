# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=' ', flush=True)
            sleep(1)
            c += p
        print('Fim da contagem!')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ', flush=True)
            sleep(1)
            c -= p
        print('Fim da contagem!')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Digite a contagem desejada: ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
