# import uteis # (maneira mais recomendada)
#
# num = int(input("Digite um valor: "))
# fat = uteis.fatorial(num)
# print(f"O fatorial de {num} é {fat}.")
# print(f"O dobro de {num} é {uteis.dobro(num)}.")
# print(f"O triplo de {num} é {uteis.triplo(num)}.")

# from uteis import fatorial, dobro, triplo (maneira menos recomendada para evitar conflito de funções)
#
# num = int(input("Digite um valor: "))
# fat = fatorial(num)
# print(f"O fatorial de {num} é {fat}.")
# print(f"O dobro de {num} é {dobro(num)}.")
# print(f"O triplo de {num} é {triplo(num)}.")

from uteis import numeros # solução com pacotes

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {numeros(num)}.")
print(f"O triplo de {num} é {numeros(num)}.")
