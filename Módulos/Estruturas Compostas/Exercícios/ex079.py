# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()

while True:
    n = int(input('Digite um número para ser inserido na lista: '))
    if n not in numeros:
        numeros.append(n)
        print(f'O número {n} foi adicionado na lista!')
    else:
        print(f'O número {n} já existe na lista!')
    r = str(input('Deseja continuar [S/N]? '))
    if r in 'Nn':
        break
numeros.sort()
print(f'A lista final ordenada fica da seguinte forma: {numeros}')
