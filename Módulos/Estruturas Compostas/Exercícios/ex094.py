# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

grupo = list()
pessoa = dict()
s = m = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Ocorreu um erro! Por favor, digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Ocorreu um erro! Por favor, digite S ou N.')
    if r == 'N':
        break
print('-'*35)
print(f'Ao todo foram cadastradas {len(grupo)} pessoas.')
m = s / len(grupo)
print(f'A média de idade é de {m:5.1f} anos')
print(f'A(s) mulher(es) cadastrada(s) foram: ', end='')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(f'A lista de pessoas que estão com idade acima da média é: ')
for p in grupo:
    if p['idade'] >= m:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='  ')
        print()
print('Programa encerrado!')