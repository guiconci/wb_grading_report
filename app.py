import dash
from dash.dependencies import Input, Output
from dash_html_components.Div import Div
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

app = dash.Dash(__name__)
server = app.server


print('Trial')

if __name__ == '__main__':
    app.run_server(debug=True)