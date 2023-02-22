# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('O número {} convertido para binário é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('O número {} convertido para octal é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('O número {} convertido para hexadecimal é igual {}'. format(num, hex(num)))
else:
    print('Opção inválida, tente novamente!')
