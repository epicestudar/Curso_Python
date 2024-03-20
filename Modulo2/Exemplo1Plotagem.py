# Importar bibliotecas necessárias
import numpy as np  # Importar a biblioteca NumPy
import pandas as pd  # Importar a biblioteca Pandas
import matplotlib.pyplot as plt  # Importar a biblioteca Matplotlib
import seaborn as sns  # Importar a biblioteca Seaborn


# Gerar dados aleatórios
np.random.seed(0)  # Definir a semente do gerador de números aleatórios do NumPy
x = np.random.randn(100)  # Gerar 100 números aleatórios com distribuição normal (média 0 e desvio padrão 1) para o eixo x
y = np.random.randn(100)  # Gerar 100 números aleatórios com distribuição normal (média 0 e desvio padrão 1) para o eixo y


# Criar DataFrame com os dados gerados
df = pd.DataFrame({'X': x, 'Y': y})  # Criar um DataFrame do Pandas com duas colunas 'X' e 'Y' contendo os dados gerados


# Plotar gráfico de dispersão com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho 8x6 polegadas
plt.scatter(df['X'], df['Y'], color='blue', alpha=0.5)  # Plotar um gráfico de dispersão com os dados do DataFrame
plt.title('Gráfico de Dispersão - Matplotlib')  # Definir o título do gráfico
plt.xlabel('X')  # Definir o rótulo do eixo x
plt.ylabel('Y')  # Definir o rótulo do eixo y
plt.grid(True)  # Habilitar a grade no gráfico
plt.show()  # Mostrar o gráfico


# Plotar gráfico de dispersão com Seaborn
plt.figure(figsize=(8, 6))  # Criar uma nova figura com tamanho 8x6 polegadas
sns.scatterplot(data=df, x='X', y='Y', color='red', alpha=0.5)  # Plotar um gráfico de dispersão com Seaborn usando os dados do DataFrame
plt.title('Gráfico de Dispersão - Seaborn')  # Definir o título do gráfico
plt.xlabel('X')  # Definir o rótulo do eixo x
plt.ylabel('Y')  # Definir o rótulo do eixo y
plt.grid(True)  # Habilitar a grade no gráfico
plt.show()  # Mostrar o gráfico

