import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml


# Carregar dados do arquivo YAML
with open('dados.yaml', 'r') as file:
    dados = yaml.safe_load(file)


# Criar DataFrame com os dados
df = pd.DataFrame(dados)


# Plotar histograma da idade com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
plt.hist(df['idade'], bins=len(df['idade']), color='skyblue', edgecolor='black')  # Plotar histograma
plt.title('Histograma da Idade - Matplotlib')  # Definir título do gráfico
plt.xlabel('Idade')  # Definir rótulo do eixo x
plt.ylabel('Frequência')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico


# Corrigir os valores na coluna 'alunos' para strings
df['alunos'] = df['alunos'].apply(lambda x: x['nome'])


# Plotar gráfico de barras das notas com Seaborn
plt.figure(figsize=(10, 6))  # Criar uma figura com tamanho específico
sns.barplot(data=df, x='alunos', y='notas', palette='pastel')  # Plotar gráfico de barras com Seaborn
plt.title('Gráfico de Barras das Notas - Seaborn')  # Definir título do gráfico
plt.xlabel('Alunos')  # Definir rótulo do eixo x
plt.ylabel('Notas')  # Definir rótulo do eixo y
plt.xticks(rotation=90)  # Rotacionar os rótulos do eixo x para melhor visualização
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico


# Plotar gráfico de dispersão da altura e idade com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
plt.scatter(df['altura'], df['idade'], color='green', alpha=0.5)  # Plotar gráfico de dispersão
plt.title('Gráfico de Dispersão da Altura e Idade - Matplotlib')  # Definir título do gráfico
plt.xlabel('Altura')  # Definir rótulo do eixo x
plt.ylabel('Idade')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico


# Plotar gráfico de dispersão da altura e idade com Seaborn
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
sns.scatterplot(data=df, x='altura', y='idade', color='purple', alpha=0.5)  # Plotar gráfico de dispersão com Seaborn
plt.title('Gráfico de Dispersão da Altura e Idade - Seaborn')  # Definir título do gráfico
plt.xlabel('Altura')  # Definir rótulo do eixo x
plt.ylabel('Idade')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico
