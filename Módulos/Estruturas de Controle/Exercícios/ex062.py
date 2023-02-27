# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.

n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = n
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(t), end=' ')
        t += r
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('\nProgressão finalizada com {} termos mostrados'.format(total))
