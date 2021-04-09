import dash
from dash.dependencies import Input, Output
from dash_html_components.Div import Div
from dash_html_components.Header import Header
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

app = dash.Dash(__name__)
server = app.server

df = pd.read_csv('https://raw.githubusercontent.com/guiconci/test_app/main/plan.csv')


app.layout = html.Div(html.H1(id='Title1',children=df['Grade']))


if __name__ == '__main__':
    app.run_server(debug=True)