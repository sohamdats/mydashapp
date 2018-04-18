import dash
import dash_html_components as html
import dash_core_components as dcc

from app import app


layout = html.Div([
              html.H4('App 1'),
              dcc.Link('Go to App 2',href='/apps/app2'),
              dcc.Link('Go home',href = '/')
              ])


