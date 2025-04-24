import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from dash import Dash,dcc,html, Input, Output

df = pd.read_csv('ecommerce_estatistica.csv')

def cria_grafico(df):
    #Historigrama
    fig1 = px.histogram(df, x='Nota', nbins=80, title="Histograma - Notas")
    fig1.update_layout(
        xaxis_title = 'Nota',
        yaxis_title = 'Quantidade'
    )

    #Dispersão
    fig2 = px.scatter(df, x='Preço', y='Qtd_Vendidos_Cod', color='Marca', hover_name='Temporada')
    fig2.update_layout(
        title='Relação entre Preço x Qtd de Vendas',
        xaxis_title='Preço',
        yaxis_title='Quantidade de Vendas'
    )
    #Mapa de Calor
    fig3 = px.density_heatmap(df, x='Preço', y='Qtd_Vendidos_Cod', color_continuous_scale='Blues', title='Mapa de Calor: Preço x Quantidade de Vendas')

    #Gráfico de Barra
    fig4 = px.bar(df, x='Gênero', color='Qtd_Vendidos_Cod', barmode='group', color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig4.update_layout(
        title='Divisão de Gênero',
        xaxis_title='Gênero',
        yaxis_title='Quantidade',
        legend_title='Quantidade de Vendas'
    )

    #Gráfico de Pizza
    contagem_generos = df['Gênero'].value_counts()
    top_n = 5

    genero_top = contagem_generos[:top_n]
    outros = contagem_generos[top_n:].sum()

    valores = list(genero_top.values) + [outros]
    labels = list(genero_top.index) + ['Outros']

    df_pizza = pd.DataFrame({'Gênero': labels, 'Quantidade': valores})

    fig5 = px.pie(df_pizza, names="Gênero", values="Quantidade",
                  title="Distribuição de Gêneros (Top 5 + Outros)",
                  color_discrete_sequence=px.colors.sequential.RdBu,
                  hole=0.1)
    fig5.update_traces(textposition='inside', textinfo='percent+label')

    #Gráfico de Densidade
    fig6 = px.density_contour(df, x='Preço', y='Desconto', title='Densidade de Preços')

    #Gráfico de Regressão Linear
    fig7 = px.scatter(df, x='Preço', y='Qtd_Vendidos_Cod', title='Regressão Linear - Preço vs Vendas')
    x = df['Preço']
    y = df["Qtd_Vendidos_Cod"]
    coef = np.polyfit(x, y, deg=1)
    regressao_y = coef[0] * x + coef[1]

    fig7.add_traces(go.Scatter(x=x, y=regressao_y, mode="lines", name="Regressão Linear", line=dict(color='red')))

    fig7.update_layout(
        xaxis_title='Preço',
        yaxis_title='Quantidade de Vendas',
        legend_title='Legenda'
    )
    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

def cria_app(df):
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6, fig7 = cria_grafico(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        dcc.Graph(figure=fig7)
    ])
    return app

if __name__ == '__main__':
    app = cria_app(df)
    app.run(debug=True, port=8050)


