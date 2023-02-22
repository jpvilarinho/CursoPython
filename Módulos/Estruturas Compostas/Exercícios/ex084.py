# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dado = list()
p_maior = p_menor = 0

while True:
    pessoas.append(str(input('Digite o nome da pessoa: ')))
    pessoas.append(float(input('Digite o peso da pessoa: ')))
    if len(dado) == 0:
        p_maior = p_menor = pessoas[1]
    else:
        if pessoas[1] > p_maior:
            p_maior = pessoas[1]
        if pessoas[1] < p_menor:
            p_menor = pessoas[1]
    dado.append(pessoas[:])
    pessoas.clear()
    r = str(input('Deseja continuar [S/N]? '))
    if r in 'Nn':
        break

print(f'Ao todo foram cadastradas {len(dado)} pessoas. ')
print(f'O maior peso foi de {p_maior}Kgs. Peso de ', end='')
for p in dado:
    if p[1] == p_maior:
        print(f'[{p[0]}] ', end='')

print()
print(f'O menor peso foi de {p_menor}Kgs. Peso de ', end='')
for p in dado:
    if p[1] == p_menor:
        print(f'[{p[0]}] ', end='')
