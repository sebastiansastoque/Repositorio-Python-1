#Contar la cantidad de elementos mayores que un valor dado en una lista:
from functools import reduce

lista = [10, 20, 30, 40, 50]
valor_limite = 25
elementos_filtrados = filter(lambda x: x > valor_limite, lista)
cantidad_elementos = reduce(lambda x, _: x + 1, elementos_filtrados, 0)

print("La cantidad de elementos mayores que", valor_limite, "en la lista es:", cantidad_elementos)
