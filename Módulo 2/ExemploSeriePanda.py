import pandas as pd

serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])


# Acessando elementos por índice
value_at_b = serie['b']
print(value_at_b)

# Fatiando a série
slice_of_series = serie[1:3]
print(slice)

# Operações matemáticas
dobro = serie * 2
print("Série multiplicada por 2:")
print(dobro)

# Filtrando dados
maior_que_30 = serie[serie > 30]
print("Elementos maiores que 30:")
print(maior_que_30)

# Operações estatísticas
media = serie.mean()
soma = serie.sum()
print("Média:", media)
print("Soma:", soma)
