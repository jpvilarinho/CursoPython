# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) ao total!')


# Programa principal
jog = str(input('Digite o nome do jogador: '))
g = str(input('Digite o número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jog.strip() == '':
    ficha(gols=g)
else:
    ficha(jog, g)
