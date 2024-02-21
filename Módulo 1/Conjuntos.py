# Criação de Conjuntos:
# Conjunto de números
numeros = {1, 2, 3, 4, 5}

# Conjunto de letras
vogais = {'a', 'e', 'i', 'o', 'u'}

# Operações de Conjuntos:
# União de conjuntos
uniao = numeros.union(vogais)  # Resultado: {1, 2, 3, 4, 5, 'a', 'e', 'i', 'o', 'u'}

# Interseção de conjuntos
intersecao = numeros.intersection({3, 4, 5, 6})  # Resultado: {3, 4, 5}

# Diferença de conjuntos
diferenca = numeros.difference({4, 5, 6})  # Resultado: {1, 2, 3}
