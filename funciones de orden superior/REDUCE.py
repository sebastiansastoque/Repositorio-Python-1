producto = 1
lista = [1,2,3,4]
for num in lista:
    producto = producto * num

#producto = 24

from functools import reduce
producto = reduce((lambda x, y: x * y) , [1,2,3,4,])

#salida 24