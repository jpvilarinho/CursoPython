def aumentar(preco=0):
    return preco + (preco * 0.1)


def diminuir(preco=0):
    return preco - (preco * 0.13)


def dobro(preco=0):
    return preco * 2


def metade(preco=0):
    return preco / 2


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>4.2f}'.replace('.', ',')
