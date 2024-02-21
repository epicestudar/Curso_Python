#Criação de Dicionários:
# Dicionário de informações sobre uma pessoa
pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

# Dicionário vazio
configuracoes = {}

# Acesso por chave
nome = pessoa['nome']  # Resultado: 'João'

# Modificação de Valores:

# Modificar um valor
pessoa['idade'] = 26  # Agora o dicionário é {'nome': 'João', 'idade': 26, 'cidade': 'São Paulo'}

# Adição e Remoção de Itens:

# Adicionar novo item
pessoa['profissao'] = 'Engenheiro'  # Resultado: {'nome': 'João', 'idade': 26, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# Remover item por chave
del pessoa['cidade']  # Resultado: {'nome': 'João', 'idade': 26, 'profissao': 'Engenheiro'}
