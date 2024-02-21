# Exercício 1 - Manipulação de Listas
numeros = [5, 3, 4, 7, 9]
numeros.sort()
print(numeros)
numeros.append(10)
print(numeros)
numeros.remove(5)
print(numeros)


# Exercício 2 - slicing e operações
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublista = numeros[1:2], numeros[3:4], numeros[5:6], numeros[7:8], numeros[9:10]
# print(sublista)
sublista[0] = 10
sublista[1] = 8
sublista[2] = 6
sublista[3] = 4
sublista[4] = 2
print(sublista)