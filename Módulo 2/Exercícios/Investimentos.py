from cProfile import label
from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios de preços médios diários para duas ações (em dólares)
preco_medio_acao1 = np.array([50, 52, 48, 55, 53, 51, 49, 50, 54, 52])
preco_medio_acao2 = np.array([120, 122, 118, 125, 123, 121, 119, 120, 124, 122])

# Número de ações que o investidor possui de cada empresa
acoes_acao1 = 100  # Exemplo: o investidor possui 100 ações da Ação 1
acoes_acao2 = 50   # Exemplo: o investidor possui 50 ações da Ação 2

# Calculando o valor do investimento em cada dia
investimento_acao1 = preco_medio_acao1 * acoes_acao1
investimento_acao2 = preco_medio_acao2 * acoes_acao2

# Calculando o patrimônio total do investidor em cada dia
patrimonio_total = investimento_acao1 + investimento_acao2

dias = list(range(1, 11))

# Exibindo os resultados diariamente
for i in range(len(preco_medio_acao1)):
    print(f'Dia {i+1}: Patrimônio total = ${patrimonio_total[i]:.2f}')

# Plotando o gráfico da evolução patrimonial do investidor
plt.plot(dias, patrimonio_total, label='Patrimônio Total', marker='o', linestyle='-', color='b')
plt.plot(dias, investimento_acao1, label='Valor Ação 1', marker='o', linestyle='-', color='r')
plt.plot(dias, investimento_acao2, label='Valor Ação 2', marker='o', linestyle='-', color='g')

plt.title('Evolução Patrimonial do Investidor')
plt.xlabel('Dias')
plt.ylabel('Patrimônio Total ($)')
plt.grid(True)
plt.legend()
plt.show()
