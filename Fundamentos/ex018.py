# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = int(input('Digite o valor do ângulo: '))
sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)
print('O valores de seno, cosseno e tangente do ângulo{}º são iguais a: {:.3f}, {:.3f} e {:.3f}'.format(ang, sen, cos,
                                                                                                        tan))
