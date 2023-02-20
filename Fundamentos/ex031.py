# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem (km): '))

if distancia > 200:
    preco = float(distancia * 0.45)
    print('O preço da viagem é igual a R${:.2f}'.format(preco))
else:
    preco = float(distancia * 0.50)
    print('O preço da viagem é igual a R${:.2f}'.format(preco))