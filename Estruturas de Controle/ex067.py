# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite o número de qual tabauada deseja ver? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('-' * 12)
print('PROGRAMA DE TABUADA ENCERRADO! TENTE NOVAMENTE!')
