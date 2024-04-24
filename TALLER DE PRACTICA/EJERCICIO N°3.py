#EJERCICIO #3Obtener el máximo elemento de una lista:
from functools import reduce

lista = [1, 5, 3, 8, 2]
maximo_elemento = reduce(lambda x, y: x if x > y else y, lista)

print("El máximo elemento de la lista es:", maximo_elemento)
