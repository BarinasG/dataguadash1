from dash import Dash, html, dcc, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px

app = Dash(__name__)

df = pd.read_table('simflows.txt')
sites = np.unique(df.site).tolist()
first = df.site[0]

app.layout = html.Div(children=[
    html.H1('Datagua Dashboard - Caudales Simulados Fondocyt 2019'),
    dcc.Dropdown(id='selected',options=sites,value=first, style={'width':"40%"}),
    dcc.Graph(id='yearlymean',figure={}),
])


@app.callback(
    Output(component_id='yearlymean', component_property='figure'),
    Input(component_id='selected', component_property='value')
)
def update_graph(selected):
    dff = df[df.site==selected]
    fig = px.line(dff,'year','mean')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
