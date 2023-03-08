# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

p = float(input('Digite o preço: R$'))
print(f'Aumentando em 10% de R${p:.2f}, temos R${moeda.aumentar(p):.2f}')
print(f'Diminuindo em 13% de R${p:.2f}, temos R${moeda.diminuir(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
