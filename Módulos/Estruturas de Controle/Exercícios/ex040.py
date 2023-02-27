# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('Média igual a {} e abaixo de 5.0: REPROVADO!'.format(m))
elif (m > 5.0) and (m < 6.9):
    print('Média igual a {} e está entre 5.0 e 6.9: RECUPERAÇÃO!'.format(m))
else:
    print('Média igual a {} e acima de 7.0: APROVADO!'.format(m))
