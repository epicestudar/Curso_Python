def calcular_media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

def calcular_mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    tamanho = len(lista_numeros)
    if tamanho % 2 == 0:
        meio1 = lista_ordenada[tamanho // 2 - 1]
        meio2 = lista_ordenada[tamanho // 2]
        return (meio1 + meio2) / 2
    else:
        return lista_ordenada[tamanho // 2]
