#Definições para o programa
import pandas as pd
import plotly.express as px
from flask import Flask, render_template
from pyparsing import col

#Função de analise de dados
def analise_dados(file_path):
    df = pd.read_csv(file_path)
    resumo = df.describe()

    fig1 = px.histogram(df, x='rating', title='Distribuição de Avaliações dos Filmes')
    fig1.write_html('templates/plot1.html')

    fig2 = px.box(df, x='genre', y='rating', title='Box Plot das Avaliações por Gênero')
    fig2.write_html('templates/plot2.html')

    fig3 = px.scatter(df, x='votes', y='rating', size='duration', color='genre', title='Relação entre Votos, Avaliações e Duração do Filme')
    fig3.write_html('templates/plot3.html')

    return resumo

def analise_dados2(file_path):
    df = pd.read_csv(file_path)
    resumo2 = df.head()

    return resumo2

# Flask Setup
app = Flask(__name__)

@app.route('/')
def index():
    resumo = analise_dados('movies.csv')
    header = analise_dados2('movies.csv')
    return render_template('index.html', resumo = resumo.to_html(), header = header.to_html())

@app.route('/plot1')
def plot1():
    return render_template('plot1.html')

@app.route('/plot2')
def plot2():
    return render_template('plot2.html')

@app.route('/plot3')
def plot3():
    return render_template('plot3.html')

if __name__ == '__main__':
    app.run(debug=True)