import streamlit as st
import pandas as pd

# titulo
st.title('Calculadora Simples')

#estrutura
num1 = st.number_input('Digite o primeiro número')

num2 = st.number_input('Digite o segundo número')

opcao = st.selectbox('Escolha a operação', ['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Potencia'])

if opcao == 'Soma':
    resultado = num1 + num2

elif opcao == 'Subtração':
    resultado = num1 - num2

elif opcao == 'Multiplicação':
    resultado = num1 * num2

elif opcao == 'Divisão':
    if num2 == 0:
        st.write('Não é possível dividir por 0')

    else:
        resultado = num1 / num2

elif opcao == 'Potencia':
    resultado = num1 ** num2

st.write(f'O resultado da operação é: {resultado}')