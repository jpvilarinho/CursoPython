# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

# #remove todos espaços em branco, passa as letras p/ maiúscula e pega somente a primeira letra da string
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo novamente [M/F]: ')).strip().upper()[0]
print('sexo {} registrado com sucesso!'.format(sexo))
