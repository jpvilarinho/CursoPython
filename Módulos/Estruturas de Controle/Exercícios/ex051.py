# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
ult = num + (10 - 1) * r

for c in range(num, (ult + r), r):
    print('{}'.format(c), end=' ')
