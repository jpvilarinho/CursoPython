# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

idade = int(input('Digite a sua idade: '))

if idade <= 9:
    print('Idade igual a {}. Categoria: MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('Idade igual a {}. Categoria: INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('Idade igual a {}. Categoria: JÚNIOR'.format(idade))
elif 19 < idade <= 25:
    print('Idade igual a {}. Categoria: SÊNIOR'.format(idade))
else:
    print('Idade igual a {}. Categoria: MASTER'.format(idade))
