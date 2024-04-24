#Concatenar todas las cadenas de una lista en una sola cadena:
from functools import reduce

lista_cadenas = ["Hola", " ", "Mundo", "!"]
cadena_concatenada = reduce(lambda x, y: x + y, lista_cadenas)

print("Lista de cadenas:", lista_cadenas)
print("Cadena concatenada:", cadena_concatenada)
