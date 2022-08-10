
def three_sum(numeros: List[int]) -> List[List[int]]:
    if len(numeros) < 3:
        return []
    numeros.sort()
    resultado = set()
    for i in range(len(numeros)-2):
        if numeros[i] <= 0:
            if i == 0 or numeros[i-1]<numeros[i]:
                mapaParejas = {}
                for num in numeros[i+1:]:
                    if num not in mapaParejas:
                        mapaParejas[-numeros[i]-num] = 1
                    else:
                        resultado.add((numeros[i], num, - numeros[i]-num))
    return [list(group) for group in resultado]


