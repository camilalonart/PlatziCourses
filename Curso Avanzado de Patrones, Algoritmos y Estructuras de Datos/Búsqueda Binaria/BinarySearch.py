def binarySearch(numeros, objetivo):
    izquierda = 0
    derecha = len(numeros) - 1 
    while izquierda <= derecha:
        mitad = izquierda + (derecha - izquierda) // 2
        if numeros[mitad] == objetivo:
            return mitad
        elif numeros[mitad] < objetivo:
            izquierda = mitad+1
        else:
            derecha = mitad-1
    return -1


    