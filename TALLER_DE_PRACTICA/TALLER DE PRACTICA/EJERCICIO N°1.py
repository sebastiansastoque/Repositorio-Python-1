#Suma de todos los elementos de una lista: 
from functools import reduce

lista = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, lista)

print("La suma de todos los elementos de la lista es:", suma_total)
