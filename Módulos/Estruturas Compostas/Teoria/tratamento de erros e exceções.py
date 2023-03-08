# print(x) a variável x não existe (exceção NameError)

# n = int(input('Número: '))
# print(f'O número digitado foi {n}') ao digitar "oito", a exceção ValueError é exibida

# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a / b
# print(f'O resultado é {r}') ao atribuir 0 para b, a exceção ZerdoDivisionError é exibida

# r = 2 / '2'
# print(r) a exceção TypeError é exibida

# lst = [3, 6, 4]
# print(lst[3]) a exceção IndexError é exibida

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmente ocorreu um erro!')
# print(f'O resultado é {r}')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmente ocorreu um erro!')
# else:
#     print(f'O resultado é {r:.1f}')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmente ocorreu um erro!')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Fim de programa!')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'Infelizmente ocorreu o erro {erro.__class__}!')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Fim de programa!')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except (ValueError, TypeError):
#     print('Infelizmente ocorreu um erro na tipagem dos dados digitado!')
# except ZeroDivisionError:
#     print('Não é possível dividir um número por zero!')
# except KeyboardInterrupt:
#     print('O usuário preferiu não informar os dados!')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Fim de programa!')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except (ValueError, TypeError):
#     print('Infelizmente ocorreu um erro na tipagem dos dados digitado!')
# except ZeroDivisionError:
#     print('Não é possível dividir um número por zero!')
# except KeyboardInterrupt:
#     print('O usuário preferiu não informar os dados!')
# except Exception as erro:
#     print(f'O erro encontrado foi {erro.__cause__}')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Fim de programa!')
