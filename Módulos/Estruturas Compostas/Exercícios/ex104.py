# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# contudo fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('ERRO! Digite um número inteiro!')
        if ok:
            break
    return valor


num = leiaInt('Digite um número inteiro: ')
print(f'O número digitado foi {num}')
