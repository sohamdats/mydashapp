import dash
import dash_html_components as html
import dash_core_components as dcc

from app import app


layout = html.Div([
              html.H4('App 2'),
              dcc.Link('Go to App 1',href='/apps/app1'),
              dcc.Link('Go home',href = '/')
              ])


