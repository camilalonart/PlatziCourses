def searchMatrix(matriz: List[List[int]], objetivo: int) -> bool:
    izquierda = 0
    derecha = len(matriz)-1
    while izquierda < derecha:                         
        mitad = izquierda + (derecha - izquierda) // 2 + 1
        if matriz[mitad][0] == objetivo:
            return True
        elif matriz[mitad][0] < objetivo:
            izquierda = mitad                     
        else:
            derecha = mitad - 1
    row = matriz[izquierda]
    izquierda = 0
    derecha = len(row) - 1
    while izquierda <= derecha:                          
        mitad = izquierda + (derecha - izquierda) // 2 
        if row[mitad] == objetivo:
            return True
        elif row[mitad] < objetivo:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1
    return False