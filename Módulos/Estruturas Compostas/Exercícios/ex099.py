# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    c = maior = 0
    print('Analisando os valores digitados...')
    sleep(1)
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if c == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        c += 1
    print(f'Foram informados {c} valor(es) ao todo!')
    print(f'O maior valor informado foi {maior}!')


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2, 3)
maior(6)
maior()
