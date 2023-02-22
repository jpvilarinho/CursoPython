# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um número para ser inserido na lista: ')))
    r = str(input('Deseja continuar [S/N]? '))
    if r in 'Nn':
        break

print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista final ordenada de forma decrescente fica da seguinte forma: {lista}')
if 5 in lista:
    print(f'O valor {5} foi encontrado na lista!')
else:
    print(f'O valor {5} não foi encontrado na lista!')
