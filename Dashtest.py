from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

opcoes = list (df["ID Loja"].unique())
opcoes.append("Todas as lojas")

app.layout = html.Div(children=[
    html.H1(children='Métricas da Loja'),
    html.H2(children= 'Analíse seus resultados'),

    html.Div(children='''
        Obs: quantidade de produtos vendidos.
    '''),

    dcc.Dropdown(opcoes, value = 'Todas as lojas', id='lista_loja'),

    dcc.Graph(
        id='vendas',
        figure=fig
    )
])

@app.callback(
    Output('vendas', 'figure'),
    Input('lista_loja', 'value')
)
def update_output(value):
    if value == 'Todas as lojas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)