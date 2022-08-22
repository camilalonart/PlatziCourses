def complejidad_lineal(lista):
    suma = 0
    multiplicacion = 1

    for numero in range(len(lista)):
        suma += numero

    for numero in range(len(lista)):
        multiplicacion *= numero

    return suma, multiplicacion