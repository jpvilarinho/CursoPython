#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
#  crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#  Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número para ser inserido na lista: ')))
    r = str(input('Deseja continuar [S/N]? '))
    if r in 'Nn':
        break
for c, n in enumerate(lista):
    if n % 2 == 0 and n != 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
print(f'A lista completa é: {lista}')
print(f'A lista dos pares é : {pares}')
print(f'A lista dos ímpares: {impares}')
