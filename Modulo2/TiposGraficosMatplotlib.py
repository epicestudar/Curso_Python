import matplotlib.pyplot as plt  # Importar a biblioteca Matplotlib
import numpy as np  # Importar a biblioteca NumPy


# Dados para o primeiro gráfico de linha
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 20]


# Plotar gráfico de linha
plt.plot(x, y)  # Plotar gráfico de linha usando os dados x e y
plt.title('Gráfico de Linha')  # Definir título do gráfico
plt.xlabel('X')  # Definir rótulo do eixo x
plt.ylabel('Y')  # Definir rótulo do eixo y
plt.show()  # Mostrar o gráfico


# Dados para o segundo gráfico de barra
categorias = ['A', 'B', 'C', 'D']
valores = [20, 35, 30, 25]


# Plotar gráfico de barra
plt.bar(categorias, valores)  # Plotar gráfico de barra usando os dados de categorias e valores
plt.title('Gráfico de Barra')  # Definir título do gráfico
plt.xlabel('Categorias')  # Definir rótulo do eixo x
plt.ylabel('Valores')  # Definir rótulo do eixo y
plt.show()  # Mostrar o gráfico


# Dados para o terceiro histograma
dados = np.random.normal(loc=0, scale=1, size=1000)


# Plotar histograma
plt.hist(dados, bins=30)  # Plotar histograma dos dados com 30 bins
plt.title('Histograma')  # Definir título do gráfico
plt.xlabel('Valores')  # Definir rótulo do eixo x
plt.ylabel('Frequência')  # Definir rótulo do eixo y
plt.show()  # Mostrar o gráfico


# Dados para o quarto gráfico de dispersão
x = np.random.randn(100)
y = np.random.randn(100)


# Plotar gráfico de dispersão
plt.scatter(x, y)  # Plotar gráfico de dispersão usando os dados x e y
plt.title('Gráfico de Dispersão')  # Definir título do gráfico
plt.xlabel('X')  # Definir rótulo do eixo x
plt.ylabel('Y')  # Definir rótulo do eixo y
plt.show()  # Mostrar o gráfico
