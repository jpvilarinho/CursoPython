# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = n
cont = 1

while cont <= 10:
    print('{}'.format(t), end=' ')
    t += r
    cont += 1
print('FIM!')


