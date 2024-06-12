import streamlit as st
import pandas as pd

st.title('Título da Aplicação')
st.header('Cabeçalho Secundário')
st.subheader('Subcabeçalho Terciário')
st.text('Este é um texto simples.')
st.markdown('**Este é um texto em negrito usando Markdown.**')
st.sidebar.title('Título na Barra Lateral')
st.sidebar.markdown('Texto na barra lateral.')
col1, col2 = st.columns(2)
col1.write('Este é o conteúdo da primeira coluna.')
col2.write('Este é o conteúdo da segunda coluna.')

#botões
if col1.button('Clique aqui'):
    col1.write('Botão clicado!')

#Caixa de seleção
if col2.checkbox('Marque-me'):
    	    col2.write('Caixa marcada!')
                
#Sliders
age = st.slider('Selecione sua idade', 0, 100, 20)
st.write(f'Sua idade é: {age}')

#inputs
nome = st.text_input('Digite seu nome')
st.write(f'Seu nome é: {nome}')

#DataFrames
data = {'Coluna 1': [1, 2, 3], 'Coluna 2': [4, 5, 6]}
df = pd.DataFrame(data)
st.write(df)

#Tabela
st.table(df)
