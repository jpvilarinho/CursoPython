# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: Um número qualquer
    :param show: Opcional. Mostra ou não a conta, dependendo do valor da variável
    :return: O valor do fatorial do número num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa principal
print(fatorial(int(input('Digite o fatorial desejado: ')), show=True))
