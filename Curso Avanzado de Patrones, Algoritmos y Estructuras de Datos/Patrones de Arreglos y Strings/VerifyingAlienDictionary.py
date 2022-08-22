def esta_ordenado(words, order):
    mapa_diccionario = {}
    for i in range(len(order)):
        mapa_diccionario[order[i]] = i

    for i in range(len(words) - 1):
        palabra1 = words[i]
        palabra2 = words[i+1]
        for j in range(min(len(palabra1), len(palabra2))):
            if palabra1[j] != palabra2[j]:
                if mapa_diccionario[palabra1[j]] > mapa_diccionario[palabra2[j]]:
                    return False
                break
        else:
            if len(palabra1) > len(palabra2):
                return False

    return True