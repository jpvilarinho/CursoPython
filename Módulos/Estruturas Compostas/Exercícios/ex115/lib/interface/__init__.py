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


def linha(tam=40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mOpção digitada: \033[m')
    return opc
