# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

L1 = float(input('Digite o valor do primeiro segmento: '))
L2 = float(input('Digite o valor do segundo segmento: '))
L3 = float(input('Digite o valor do terceiro segmento: '))

TRI = (L1 < L2 + L3) and (L2 < L1 + L3) and (L3 < L1 + L2)
EQ = (L1 == L2) and (L2 == L3) and (L1 == L3)
ESC = (L1 != L2) and (L2 != L3) and (L1 != L3)
ISO = (L1 == L2) or (L2 == L3) or (L1 == L3)

if TRI:
    print('É possível formar um triângulo')
    if TRI == EQ:
        print('O triângulo é EQUILÁTERO!')
    elif TRI == ISO:
        print('O triângulo é ISÓCELES!')
    elif TRI == ESC:
        print('O triângulo é ESCALENO!')
else:
    print('Os segmentos não formam um triângulo')

