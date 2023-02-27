frase = '   Curso em Vídeo Python   '
print(frase) # imprime a frase
print(frase.strip()) # imprime a frase sem espaços em branco à direita e à esquerda
print(frase.rstrip()) # imprime a frase sem espaços em branco à direita
print(frase.lstrip()) # imprime a frase sem espaços em branco à esquerda
print(frase.upper().count('O')) # faz a contagem na quantidade de letras 'O' na frase com letras maiúsculas
print(frase[3:13]) # imprime a frase da 4ª até a 12ª posição
print(frase[:13]) # imprime a frase do início até a 12ª posição
print(frase[13:]) # imprime a frase da 12ª posição até o final
print(frase[1:15:2]) # imprime a frase da posição 0 até a 14ª posição, pulando de duas em duas posições
print(frase[1::2]) # imprime a frase da 1ª posição até o final, pulando de duas em duas posições
print(frase[::2]) # imprime a frase do início até o final, pulando de duas em duas posições
print(len(frase)) # imprime o tamanho da frase
print(frase.replace('Python', 'Android')) # substitui informação da string
print(frase.upper()) # imprime a frase com letras maiúsculas
print(frase.lower()) # imprime a frase com letras minúsculas
print(frase.capitalize()) # imprime a frase com a primeira letra maiúscula
print(frase.title()) # imprime a frase com todas as palavras com letra maiúscula
print(frase.split()) # separa as palavras da string em uma lista
print('-'.join(frase)) # separa as letras da string com o símbolo '-'
print(len(frase.strip())) # imprime o tamanho da frase formatada, sem espaços no início e no fim
frase = frase.replace('Python', 'Android') # atribuição da substituição da informação na string na variável frase
print(frase) # imprime a frase com informação substituída
print('Curso' in frase) # imprime se a informação está presente na string
print(frase.lower().find('vídeo')) # imprime a frase com letras minúsculas e encontra a posição em a palavra se inicia
dividido = frase.split() # atribuição de split da frase para a variável 'dividido'
print(dividido[2][3]) # imprime o terceiro elemento da terceira posição da lista
