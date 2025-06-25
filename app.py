# app.py
import dash
from dash.dependencies import Input, Output
import dash_table
from dash_table import DataTable, FormatTemplate
import dash_core_components as dcc
from dash import html
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