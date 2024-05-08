# Convertir una lista de cadenas a una lista de enteros:
lista_cadenas = ["1", "2", "3", "4", "5"]
lista_enteros = list(map(lambda x: int(x), lista_cadenas))

print("Lista original de cadenas:", lista_cadenas)
print("Lista de enteros:", lista_enteros)