# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

from time import sleep

alunos = list()

while True:
    nome = (str(input('Nome do aluno: ')))
    nota1 = (float(input('Digite a primeira nota do aluno: ')))
    nota2 = (float(input('Digite a segunda nota do aluno: ')))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar [S/N]? '))
    if r in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for a, b in enumerate(alunos):
    print(f'{a:<4}{b[0]:<10}{b[2]:>8.1f}')
while True:
    op = int(input('Mostrar as notas de qual aluno?  (Digite 9 p/ interromper): '))
    if op == 9:
        sleep(1)
        print('Finalizando...')
        break
    if op <= len(alunos) - 1:
        print(f'Notas de {alunos[op][0]} são {alunos[op][1]}')
print('Programa finalizado!')

