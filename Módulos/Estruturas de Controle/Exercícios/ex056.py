# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

s_idade = 0
m_idade = 0
maior_idade_homem = 0
nome_homem_velho = ''
mulher_menos_vinte = 0

for p in range(1, 5):
    print('----------{}ª PESSOA----------'.format(p))
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    s_idade += idade

    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if idade < 20 and sexo in 'Ff':
        mulher_menos_vinte += 1

m_idade = s_idade / 4
print('A média de idade é igual a: {}'.format(m_idade))
print('O homem mais velho possui {} anos e ele se chama {}'.format(maior_idade_homem, nome_homem_velho))
print('A quantidade de mulheres com menos de vinte anos é igual a {}'.format(mulher_menos_vinte))
