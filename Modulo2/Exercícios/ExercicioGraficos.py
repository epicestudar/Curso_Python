import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados do arquivo Excel
df_filmes = pd.read_excel('Modulo2/filmes.xlsx')

# Contar o número de filmes por gênero
contagem_genero = df_filmes['Genero'].value_counts()

# Criar gráfico de barras
plt.figure(figsize=(10, 6))
contagem_genero.plot(kind='bar', color='skyblue')
plt.title('Contagem de Filmes por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Filmes')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
