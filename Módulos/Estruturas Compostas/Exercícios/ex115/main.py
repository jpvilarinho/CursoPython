# Vamos criar um menu em Python, usando modularização.

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resp = menu(['Cadastrar uma pessoa nova', 'Ver lista de pessoas cadastradas', 'Sair do programa'])
    if resp == 1:
        # Opção de cadastrar uma nova pessoa
        cabecalho('Novo Cadastro!')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 2:
        # Opção de listar o conteúdo de um arquivo
        lerArq(arq)
    elif resp == 3:
        # Opção de sair do sistema
        print(linha())
        cabecalho('Saindo do sistema, fim do programa!')
        print(linha())
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
