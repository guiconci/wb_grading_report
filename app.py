import dash
from dash.dependencies import Input, Output
from dash_html_components.Div import Div
import dash_table
from dash_table import DataTable, FormatTemplate
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from quick_srt import df, df2

app = dash.Dash(__name__)
server = app.server

df.set_index('id',inplace=True, drop=False)


df2.set_index('id',inplace=True, drop=False)


app.layout = html.Div(html.H1(id='Title1',children=df['Grade']))


if __name__ == '__main__':
    app.run_server(debug=True)