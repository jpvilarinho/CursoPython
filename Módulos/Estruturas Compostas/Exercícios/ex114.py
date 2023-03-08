#  Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.uol.com.br')
except urllib.error.URLError:
    print(f'O site não está acessível no momento!')
else:
    print(f'O site foi acessado com sucesso!!')

