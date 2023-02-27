# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantidade de dias que o carro foi alugado: '))
dist = float(input('Distância percorrida, em km: '))
c_dias = dias * 60
c_dist = dist * 0.15
a = c_dias + c_dist
print('O valor total do aluguel do veículo é igual: R${:.2f}'.format(a))
