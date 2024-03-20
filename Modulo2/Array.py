import numpy as np

array_vazio = np.empty((3, 3)) # matriz 3x3 vazia
print(array_vazio)

ones_array = np.ones((2, 2)) # matriz 2x2 preenchidas por 1
print(ones_array)

zeros_array = np.zeros((4, 4)) # matriz 4x4 preenchida por 0
print(zeros_array)

random_array = np.random.rand(3, 3) # criando uma matriz 3x3 com valores aleatórios
print(random_array)

my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array[1, 2])  # Seleciona o elemento na segunda linha e terceira coluna (6)

max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

total_sum = np.sum(my_array) # soma tudo
print(f"Soma total: {total_sum}")

squeezed_array = np.squeeze(my_array) # remove entradas unidimensionais
print(squeezed_array)

# adição de matrizs
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

# subtração de matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)


# multiplicação de matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)

diagonal_sum = np.trace(my_array) # soma os elementos das diagonais da matriz
print(f"Soma diagonal: {diagonal_sum}")

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_linhas, num_colunas = np.shape(matriz)
print(f"Número de linhas: {num_linhas}")
print(f"Número de colunas: {num_colunas}")

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linha_especifica = np.array([4, 5, 6])
contem_linha = np.isin(matriz, linha_especifica).all(axis=1).any()
print(f"Contém a linha específica? {contem_linha}")



matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # troca dois eixos da matriz
matriz_transposta = np.transpose(matriz)
# Ou, alternativamente: matriz_transposta = matriz.T
print("Matriz original:")
print(matriz)
print("Matriz transposta:")
print(matriz_transposta)
