# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mO usuário não digitou o número inteiro!\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mO usuário não digitou o número real!\033[m')
            return 0
        else:
            return num


num_1 = leiaInt('Digite um número inteiro: ')
num_2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {num_1} e o número real foi {num_2}')
