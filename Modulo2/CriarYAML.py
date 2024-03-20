import yaml


# Dados iniciais
dados_iniciais = {
    'alunos': ['João', 'Maria', 'Pedro', 'Ana', 'Carla'],
    'notas': [8, 7, 9, 6, 8],
    'idade': [20, 22, 21, 19, 20],
    'altura': [1.75, 1.65, 1.80, 1.70, 1.68]
}


# Expandir os dados para 100 registros
dados_expandidos = {
    'alunos': [],
    'notas': [],
    'idade': [],
    'altura': []
}


# Repetir os dados iniciais para criar 100 registros
for i in range(100):
    for key, value in dados_iniciais.items():
        dados_expandidos[key].append(value[i % len(value)])


# Salvar os dados expandidos em um arquivo YAML
with open('dados.yaml', 'w') as file:
    yaml.dump(dados_expandidos, file)


print("Arquivo YAML com dados expandidos criado com sucesso!")
