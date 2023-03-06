# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade >= 18:
        print(f'Com {idade} anos, o voto é OBRIGATÓRIO!')
    elif 17 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos, o voto é OPCIONAL!')
    else:
        print(f'Com {idade} anos, o voto é NEGADO!')


#Programa principal
ano_nasc = int(input('Digite o ano de nascimento: '))
print(voto(ano_nasc))
