# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot_gols = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou: '))
    partidas.clear()

    for c in range(0, tot_gols):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Ocorreu um erro! Por favor, digite S ou N.')
    if r == 'N':
        break
print('-'*55)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for a in v.values():
        print(f'{str(a):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (Digite 9 para parar): '))
    if busca == 9:
        break
    if busca >= len(time):
        print(f'Ocorreu um erro! Não existe jogador com o código {busca}')
    else:
        print(f'     APROVEITAMENTO DO JOGADOR {time[busca]["nome"]}:     ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'       No jogo {i+1}, fez {g} gols')
        print('-'*40)
    print('Programa encerrado!')
