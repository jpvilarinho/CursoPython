# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer, {}!'.format(n))
print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu último nome é: {}'.format(nome[len(nome)-1]))
