def search(numeros: List[int], objetivo: int) -> int:
    izquierda = 0
    derecha = len(numeros) - 1
    while izquierda <= derecha:
        mitad = izquierda + (derecha-izquierda) // 2
        if numeros[mitad] == objetivo:
            return mitad
        elif numeros[mitad] >= numeros[izquierda]:
            if objetivo >= numeros[izquierda] and objetivo < numeros[mitad]:
                derecha = mitad- 1
            else:
                izquierda = mitad + 1
        else:
            if objetivo <= numeros[derecha] and objetivo > numeros[mitad]: 
                izquierda = mitad + 1
            else:
                derecha = mitad -  1
    return -1