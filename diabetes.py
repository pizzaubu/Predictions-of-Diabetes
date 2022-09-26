import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

from dash.dependencies import Input, Output

df = pd.read_csv("D:\__MACOSX\pythonProject1\diabetes.csv")

app = dash.Dash(__name__)
server=app.server

app.layout = html.Div([
    html.H4('Prediction of diabetes'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label':'Pregnancies','value':'Pregnancies'},
        {'label':'Glucose','value':'Glucose'},
        {'label':'BloodPressure','value':'BloodPressure'},
        {'label':'SkinThickness','value':'SkinThickness'},
        {'label':'Insulin','value':'Insulin'},
        {'label':'BMI','value':'BMI'},
        {'label':'DiabetesPedigreeFunction','value':'DiabetesPedigreeFunction'},
        {'label':'Age','value':'Age'},
        {'label':'Outcome','value':'Outcome'}],
        value=['Age','Insulin','BMI'],
        multi = True
    ),
    dcc.Graph(id='graph'),
])

@app.callback(
    Output('graph','figure'),
    Input('dropdown','value'))

def update_bar_chart(dims):
    fig=px.scatter_matrix(
        df,dimensions=dims)
    return fig


if __name__ == '__main__':
    app.run_server(debug=False,host="0.0.0.0", port=8080)
