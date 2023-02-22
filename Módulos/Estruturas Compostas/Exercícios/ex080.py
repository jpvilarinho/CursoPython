# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados ficam da seguinte maneira em ordem: {lista}')

# Solução alternativa
# numeros = [int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
#            int(input('Digite o pénúltimo número: ')), int(input('Digite o último número: '))]
# print(f'A lista antes de ser ordenada está da seguinte forma: {numeros}')
#
# for c in range(len(numeros)):
#     for j in range(len(numeros) - 1):
#         if numeros[j] > numeros[j+1]:
#             numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
#
# print(f'A lista ordenada fica da seguinte forma: {numeros}')
