def busqueda_binaria(lista):
    apuntador_izquierdo = 0
    apuntador_derecho = len(nums) - 1 
    
    while apuntador_izquierdo <= apuntador_derecho:
        mitad = (apuntador_izquierdo+apuntador_derecho) // 2
        if nums[mitad] == target:
            return mitad
        elif nums[mitad] < target:
            apuntador_izquierdo = mitad + 1
        else: 
            apuntador_derecho = mitad - 1
    return -1

    