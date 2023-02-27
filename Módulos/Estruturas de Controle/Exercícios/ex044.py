# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

val = float(input('Digite o valor do produto: R$'))
print('''Escolha uma das bases para conversão:
[ 1 ] Pagamento à vista no dinheiro/cheque
[ 2 ] Pagamento à vista no cartão
[ 3 ] Pagamento em até 2x no cartão
[ 4 ] Pagamento em 3x ou mais no cartão''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('O valor final do produto é igual R${:.2f}'.format(val - val * 0.10))
elif opcao == 2:
    print('O valor final do produto é igual R${:.2f}'.format(val - val * 0.05))
elif opcao == 3:
    print('O valor final do produto é igual R${:.2f}'.format(val))
elif opcao == 4:
    print('O valor final do produto é igual {:.2f}'.format(val + val * 0.20))
else:
    print('Opção inválida, tente novamente!')
