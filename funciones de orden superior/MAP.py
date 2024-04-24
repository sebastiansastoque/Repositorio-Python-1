def multiple(numero):

    if numero % 5== 0:

        return True
    
    else:
        return False
numero = [2,5,10,23,50,33]
resultados = []

for num in numero:

    resultados.append(multiple(num))

print(resultados)