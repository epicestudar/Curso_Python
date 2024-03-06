import cmath

# Crie três variáveis, a, b e c, representando os coeficientes de uma equação quadrática (ax^2 + bx + c). Calcule as raízes da equação usando a fórmula de Bhaskara.
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

delta = cmath.sqrt(b ** 2 - 4 * a * c)
raiz1 = (-b + delta) / (2 * a)
raiz2 = (-b - delta) / (2 * a)

print(f"As raízes quadráticas são: {raiz1} e {raiz2}")

# Implemente um programa que converta um valor em dólares para outras moedas (por exemplo, euros e libras). Solicite ao usuário o valor em dólares e a taxa de conversão.

dolares = float(input("Digite o valor em dólares: "))
taxa_conversao = float(input("Digite a taxa de conversão: "))

euros = dolares * taxa_conversao
libras = dolares * 0.75

print(f"Em euros: {euros: .2f}")
print(f"Em libras: {libras: .2f}")

# Crie uma função que receba uma string como entrada e retorne True se ela for um palíndromo (lê-se igual de trás para frente), e False caso contrário.
def palindromo(texto):
    texto = texto.lower().replace("", "")
    return texto == texto[::-1]

frase_usuario = input("Digite uma frase: ")
resultado_palindromo = palindromo(frase_usuario)
print(f"A frase é um palindromo: {resultado_palindromo}")