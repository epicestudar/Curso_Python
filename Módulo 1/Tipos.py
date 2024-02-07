# Números inteiros
from networkx import krackhardt_kite_graph


idade = 25
quantidade_produtos = 100

# Números de ponto flutuante
preco_unitario = 29.99
pi = 3.14159

# Strings simples
nome = "Alice"
mensagem = 'Olá, seja bem-vindo!'

# Concatenação de strings
nome_completo = nome + " Wonderland"

# Formatação de strings
mensagem_formatada = f"Olá, {nome}! Você tem {idade} anos."

# Listas (mutáveis)
frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4, 5]

# Adicionando elementos a uma lista
frutas.append("laranja")

# Tuplas (imutáveis)
coordenadas = (4, 5)
cores_rgb = (255, 0, 0)

# Dicionário chave-valor
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "engenheiro"
}

# Acessando valores
print(pessoa["nome"])
print(pessoa.get("idade"))

# Adicionando novo par chave-valor
pessoa["cidade"] = "São Paulo"
