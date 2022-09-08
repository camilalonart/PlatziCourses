def minKnightMoves(origenX, origenY, objetivoX, objetivoY):
    directions = [[-1,2],[1,2],[-1,-2],[1,-2],[-2,1],[2,1],[-2,-1],[2,-1]]
    visitados = set()
    queue = [[origenX, origenY]]
    nivel = 0
    while queue:
        for _ in range(len(queue)):
            actualX, actualY = queue.pop(0)
                if objetivoX == currentX and objetivoY == actualY: return nivel
            if (currentX, actualY) in visitados: continue
            visitados.add((currentx, actualY))
            for direction in directions:
                queue.append(actualX + direction[0], actualY + direction[1])
        nivel+=1
    return -1