# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# print(pessoas[0])

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# print(pessoas['nome'])
#
# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# print(pessoas['idade'])

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# print(f'O {pessoas['nome']}.')

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# print(pessoas.keys())

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# print(pessoas.values())

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# print(pessoas.items())

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# for k in pessoas.keys():
#     print(k)

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# for v in pessoas.values():
#     print(v)

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# del pessoas['sexo']
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# pessoas['nome'] = 'Pedro'
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 28}
# pessoas['peso'] = 82.2
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'UF':'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'UF':'São Paulo', 'Sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['UF'])
# print(brasil[1]['Sigla'])

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['UF'] = str(input('Unidade Federativa: '))
#     estado['Sigla'] = str(input('Sigla do estado: '))
#     brasil.append(estado) # nesse caso, adicionar os elementos no dicionário não reflete no resultado da lista
# print(brasil)

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['UF'] = str(input('Unidade Federativa: '))
#     estado['Sigla'] = str(input('Sigla do estado: '))
#     brasil.append(estado[:]) # não é possível fazer fatiamento de strings em dicionários!
# print(brasil)

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['UF'] = str(input('Unidade Federativa: '))
#     estado['Sigla'] = str(input('Sigla do estado: '))
#     brasil.append(estado.copy())  # forma correta de criar uma cópia dos elementos para um dicionário
# print(brasil)

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['UF'] = str(input('Unidade Federativa: '))
#     estado['Sigla'] = str(input('Sigla do estado: '))
#     brasil.append(estado.copy()) 
# print(brasil)
# for e in brasil:
#     print(e)

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['UF'] = str(input('Unidade Federativa: '))
#     estado['Sigla'] = str(input('Sigla do estado: '))
#     brasil.append(estado.copy())  # forma correta de criar uma cópia dos elementos para um dicionário
# for e in brasil:
#     for k, v in e.items():
#         print(f'O campo {k} tem valor {v}')

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['UF'] = str(input('Unidade Federativa: '))
#     estado['Sigla'] = str(input('Sigla do estado: '))
#     brasil.append(estado.copy())  # forma correta de criar uma cópia dos elementos para um dicionário
# for e in brasil:
#     for v in e.values():
#         print(f'{v}', end=' ')
#     print()
