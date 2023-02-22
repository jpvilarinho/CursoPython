# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um outro valor: '))

opcao = 0

while opcao != 5:
    print('''Escolha uma das opções abaixo: 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} + {} é igual a {}'.format(v1, v2, soma))
    elif opcao == 2:
        mult = v1 * v2
        print('A multiplicação entre {} x {} é igual a {}'.format(v1, v2, mult))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
            print('O maior valor entre {} e {} é igual a {} '.format(v1, v2, maior))
        else:
            maior = v2
            print('O maior valor entre {} e {} é igual a {}'.format(v1, v2, maior))
    elif opcao == 4:
        print('Informe os números novamente!')
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite um outro valor: '))
    elif opcao == 5:
        print('Saindo do programa. Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. tente novamente!')
    sleep(1)
print('Programa finalizado!')
