def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcula o aumento no preço de um determinado produto.
    :param preco: O preço a ser reajustado.
    :param taxa: Referente a taxa de reajuste.
    :param formato: Define se a saída será formatada ou não.
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxa_aum=0, taxa_desc=0):
    print('-'*30)
    print('RESUMO DE VALORES'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'Com {taxa_aum}% de aumento: \t{aumentar(preco, taxa_aum, True)}')
    print(f'Com {taxa_desc}% de desconto: \t{diminuir(preco, taxa_desc, True)}')
    print(f'Dobro do preço: \t\t{dobro(preco, True)}')
    print(f'Metade do preço: \t\t{metade(preco, True)}')
