import streamlit as st
import pandas as pd

df = pd.read_csv('movies.csv')

st.write(df.head())

filtro = st.sidebar.selectbox('Selecione o filtro', df.columns)