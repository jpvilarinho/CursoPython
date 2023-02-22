# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]
num = 0

for c in range(1, 8):
    num = (int(input('Digite um número: ')))
    if num % 2 == 0 and num != 0:
        numeros[0].append(num)
    elif num % 2 == 1 and num != 0:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados em ordem crescente são: {numeros[0]}')
print(f'Os valores ímpares digitados em ordem crescente são: {numeros[1]}')

