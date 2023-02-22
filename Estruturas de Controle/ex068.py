# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

j = 0

while True:
    par_impar_jogador = int(input('Diga um valor: '))
    par_impar_pc = randint(0, 10)
    total = par_impar_jogador + par_impar_pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()
    print(f'Você jogou {par_impar_jogador} e o computador {par_impar_pc}. Total de {total} ', end='')
    print(f'= PAR' if total % 2 == 0 else '= ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            j += 1
        else:
            print('Você perdeu!')
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            j += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente!')