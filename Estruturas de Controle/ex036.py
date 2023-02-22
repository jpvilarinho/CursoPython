# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.

preco = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = preco / (anos * 12)

if prest > 0.3 * sal:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(preco, anos, prest))
    print('A prestação excede 30% do valor do salário. Nesse caso, o empréstimo será negado!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(preco, anos, prest))
    print('A prestação não excede 30% do valor do salário. Nesse caso, o empréstimo será concedido!')
