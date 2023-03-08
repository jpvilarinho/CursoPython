# Modifique as funções criadas no desafio 107 para elas aceitarem um parâmetro a mais, informando
# se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

p = float(input('Digite o preço: R$'))
print(f'Aumentando em 10% de {moeda.moeda(p)}, temos R${moeda.aumentar(p, True)}')
print(f'Diminuindo em 13% de {moeda.moeda(p)}, temos R${moeda.diminuir(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
