# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade atual do carro(Km/h)? '))

if v > 80:
    m = float(7 * (v - 80))
    print('Você foi multado! O valor da multa é igual a R${:.2f}'.format(m))
else:
    print('Tenha um bom dia! Dirija com segurança!')