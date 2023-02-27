# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

L1 = float(input('Digite o primeiro segmento: '))
L2 = float(input('Digite o segundo segmento: '))
L3 = float(input('Digite o terceiro segmento: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Os segmentos {}, {} e {} podem formar um triângulo!'.format(L1, L2, L3))
else:
    print('O segmentos {}, {} e {} não podem formar um triângulo!'.format(L1, L2, L3))
