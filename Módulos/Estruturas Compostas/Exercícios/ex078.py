# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = [int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
           int(input('Digite o pénúltimo número: ')), int(input('Digite o último número: '))]

print(numeros)
print(f'O maior valor digitado na lista é {max(numeros)} e está na {numeros.index(max(numeros))+1}ªposição')
print(f'O maior valor digitado na lista é {min(numeros)} e está na {numeros.index(min(numeros))+1}ªposição')
