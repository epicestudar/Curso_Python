#Criação de Listas:

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista de strings
frutas = ["maçã", "banana", "laranja"]

# Lista mista
misturada = [1, "python", True, 3.14]


#Acesso a Elementos:

# Acesso por índice
primeiro_elemento = numeros[0]  # Resultado: 1

# Índices negativos contam a partir do final
ultimo_elemento = frutas[-1]  # Resultado: "laranja"

#Modificação de Elementos:

# Modificar um elemento
frutas[1] = "kiwi"  # Agora a lista é ["maçã", "kiwi", "laranja"]

#Adição e Remoção de Elementos:

# Adicionar elemento ao final da lista
frutas.append("uva")  # Resultado: ["maçã", "kiwi", "laranja", "uva"]

# Remover elemento por valor
frutas.remove("kiwi")  # Resultado: ["maçã", "laranja", "uva"]
