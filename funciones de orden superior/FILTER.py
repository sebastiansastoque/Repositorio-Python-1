def es_par(n):
    return n % 2 == 0

listas_pares = list(filter(es_par, range(1, 51)))

print(listas_pares)