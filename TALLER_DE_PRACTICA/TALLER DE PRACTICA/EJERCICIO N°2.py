#Multiplicación de todos los elementos de una lista:
from functools import reduce

lista = [1, 2, 3, 4, 5]
producto_total = reduce(lambda x, y: x * y, lista)

print("El producto de todos los elementos de la lista es:", producto_total)