import random

# Exercicio 1
numeros = []
for i in range(5):
    numero = random.randint(1, 100)
    numeros.append(numero)

print("Os números gerados são:")
for numero in numeros:
    print(numero)

# Exercício 2
numeros = []
for i in range(10):
    numero = random.randint(1, 100)
    numeros.append(numero)

print(f"Os números gerados são: {numeros}")

for numero in reversed(numeros):
    print(f"Ordem inversa: {numero}")

# Exercício 3 - NÃO FINALIZADO
notas = []
for i in range(4):
    nota = random.randint(0, 10)
    notas.append(nota)

print(f"Notas: {notas}")

for nota in notas:
    media = (nota + nota + nota + nota) / 4
    print(media)