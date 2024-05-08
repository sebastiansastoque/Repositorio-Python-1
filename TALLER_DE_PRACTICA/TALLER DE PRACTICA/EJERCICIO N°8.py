# Multiplicar todos los números pares de una lista:
from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(lambda x: x % 2 == 0, lista)
producto_pares = reduce(lambda x, y: x * y, numeros_pares, 1)

print("El producto de todos los números pares en la lista es:", producto_pares)
