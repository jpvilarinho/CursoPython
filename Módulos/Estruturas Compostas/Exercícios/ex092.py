# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
pessoa = dict()

pessoa['nome'] = str(input('Digite o nome: '))
ano_nasc = int(input('Digite o ano de nascimento: '))
pessoa['idade'] = date.today().year - ano_nasc
pessoa['ctps'] = int(input('Digite a carteira de trabalho (Digite 0 caso não tenha): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite o salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - date.today().year)
for k, v in pessoa.items():
    print(f'{k} tem o valor igual a {v}')
