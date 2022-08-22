def trap(alturas) -> int:
    if not alturas: return 0
    izquierda = 0
    alturaMaxIzquierda = 0
    derecha = len(alturas) - 1
    alturaMaxDerecha = 0
    aguaAtrapada = 0
    while izquierda < derecha:
        if alturas[izquierda] < alturas[derecha]:
            if alturas[izquierda] > alturaMaxIzquierda:
                alturaMaxIzquierda = alturas[izquierda]
            else:
                aguaAtrapada+= alturaMaxIzquierda - alturas[izquierda] 
            izquierda+=1
        else:
            if alturas[derecha] > alturaMaxDerecha:
                alturaMaxDerecha = alturas[derecha]
            else:
                aguaAtrapada+= alturaMaxDerecha - alturas[derecha] 
            derecha -= 1
    return aguaAtrapada