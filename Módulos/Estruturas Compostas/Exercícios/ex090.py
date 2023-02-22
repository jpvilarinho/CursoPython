# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['Média'] <= 6.9:
    aluno['Situação'] = 'Recuperação!'
else:
    aluno['Situação'] = 'Reprovado!'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
