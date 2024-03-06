# Exercício 1 - operações com números
a = input("Digite um n°: ")
b = input("Digite outro n°: ")

a = int(a)
b = int(b)

soma = (a) + (b)
subtracao = (a) - (b)
multiplicacao = (a) * (b)
divisao = (a) / (b)
resto = (a) % (b)
potencia = (a) ** (b)
print("Soma: " + str(soma))
print("Subtração: " + str(subtracao))
print("Multiplicação: " + str(multiplicacao))
print("Divisão: " + str(divisao))
print("Resto: " + str(resto))
print("Potência: " + str(potencia))

raio_circulo = 5
calcular_area = float(3.14 * raio_circulo)**2
print(calcular_area)

# Exercício 2 - concatenando strings
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)

frase = "O dia está ensolarado"
frase_upper = frase.upper()
frase_lower = frase.lower()
frase_substituida = frase.replace("ensolarado", "nublado")
print(frase_upper)
print(frase_lower)
print(frase_substituida)

# Exercício 3 - Utilização de Listas e Tuplas
cores = ["vermelho", "azul", "amarelo"]
cores.append("roxo")
cores.append("laranja")
print(cores)

coordenadas = (120, 50)
print(coordenadas[0])
print(coordenadas[1])

# Exercício 4 - estruturas condicionais
a = input("Digite um n°: ")
b = input("Digite outro n°: ")

a = int(a)
b = int(b)

if a % 2 == 0 and b % 2 == 0:
    print("Ambos os números são pares.")
else:
    print("Pelo menos um dos números não é par.")

idade = input("Qual a sua idade?")
idade = int(idade)
if idade >=18 and idade <=65:
    print("Idade aceita")
elif idade < 18:
    print("Toddynho")
elif idade > 65:
    print("Dinossauro")


numeros = [1, 3, 6, 9, 12, 15]

for numero in numeros:
    if numero % 3 == 0 and numero % 2 != 0:
        print(f"{numero} é múltiplo de 3")