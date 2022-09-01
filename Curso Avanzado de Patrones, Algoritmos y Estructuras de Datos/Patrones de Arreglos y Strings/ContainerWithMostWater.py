c def maxArea(self, height: List[int]) -> int:
    areaMaxima = 0
    izquierda = 0
    derecha = len(height)-1
    while izquierda < derecha:
        currentArea = min(height[izquierda], height[derecha]) * (derecha - izquierda)
        areaMaxima = max (currentArea, areaMaxima)
        if height[izquierda] < height[derecha]:
            izquierda+=1
        else:
            derecha-=1
    return areaMaxima