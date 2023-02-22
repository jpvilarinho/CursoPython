# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade_alist = 18
idade = ano_atual - ano_nasc
dif = idade_alist - idade
dif_2 = idade - idade_alist

if idade < idade_alist:
    print('Você possui {} anos e ainda faltam {} ano(s) para poder se alistar'.format(idade, dif))
elif idade > idade_alist:
    print('Você possui {} anos e já passou {} ano(s) da fase de alistamento'.format(idade, dif_2))
elif idade == idade_alist:
    print('Você possui {} anos e já pode se alistar!'.format(idade))
