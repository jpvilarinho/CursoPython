# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_j = maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz [i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]
    print()
print(f'A soma de valores pares é: {soma_par}')
for i in range(0, 3):
    soma_j += matriz[i][2]
print(f'A soma do valores da terceira columa é: {soma_j}')
for j in range(0, 3):
    if j == 0:
        maior = matriz[1][j]
print(f'O maior valor da segunda linha: {maior}')
