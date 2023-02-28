# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot_gols = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou: '))

for c in range(0, tot_gols):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print('-'*55)
print(jogador)
print('-'*55)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
print('-'*30)
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, {jogador["nome"]} fez {v} gols')
print(f'O total de gols é igual a {jogador["total de gols"]} gols')
