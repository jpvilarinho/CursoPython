# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
# valor monetário formatado.

import moeda

p = float(input('Digite o preço: R$'))
print(f'Aumentando em 10% de {moeda.moeda(p)}, temos R${moeda.moeda(moeda.aumentar(p))}')
print(f'Diminuindo em 13% de {moeda.moeda(p)}, temos R${moeda.moeda(moeda.diminuir(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')

