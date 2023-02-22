# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste)
# print(teste)
# print(galera)
#
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste)
# print(galera)

# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera)
# print(galera[0])
# print(galera[0][0])
# print(galera[2][1])
# print(galera[3][0])

# for pessoa in galera:
#     print(pessoa)

# for pessoa in galera:
#     print(pessoa[0])

# for pessoa in galera:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

# galera = list()
# dado = list()
# for c in range (0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado)
#     dado.clear()
# print(galera)

# galera = list()
# dado = list()
# for c in range (0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
#
# print(galera)

# galera = list()
# dado = list()
# totmai = totmen = 0
# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
#
# print(galera)
#
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade!')
#         totmai += 1
#     else:
#         print(f'{p[0]} é menor de idade!')
#         totmen += 1
#
# print(f'temos {totmai} maior(es) de idade e {totmen} menor(es) de idade.')