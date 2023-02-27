# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

v_real = float(input('Digite quantos R$ você possui na carteira: '))
v_dolar = v_real / 5.17
print('Com R${:.2f}, você consegue comprar U${:.2f}!'.format(v_real, v_dolar))
