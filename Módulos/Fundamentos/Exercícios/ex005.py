# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1
print('O antecessor e sucessor do número {} são: {} e {}'.format(num, ant, suc))
