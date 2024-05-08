# Filtrar números pares de una lista y luego calcular su suma:
from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(lambda x: x % 2 == 0, lista)
suma_pares = reduce(lambda x, y: x + y, numeros_pares, 0)

print("La suma de los números pares en la lista es:", suma_pares)
