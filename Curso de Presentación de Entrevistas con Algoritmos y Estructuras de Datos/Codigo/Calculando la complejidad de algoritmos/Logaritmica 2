def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        izquierdo = arr[:mid]
        derecho = arr[mid:]
        merge_sort(izquierdo)
        merge_sort(derecho)
        i = j = k = 0
        while i < len(izquierdo) and j < len(derecho):
            if izquierdo[i] < derecho[j]:
                arr[k] = izquierdo[i]
                i += 1
            else:
                arr[k] = derecho[j]
                j += 1
            k += 1

        while i < len(izquierdo):
            arr[k] = izquierdo[i]
            i += 1
            k += 1
 
        while j < len(derecho):
            arr[k] = derecho[j]
            j += 1
            k += 1