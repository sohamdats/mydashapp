import dash
from dash.dependencies import Output,Input,Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from pymongo import MongoClient
from time import sleep
import numpy as np

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    
     html.Div(children=[
         html.Div(html.Button(id ='click-me',children='Click Me',className='btn btn-primary',n_clicks=0),className='col-md-1'),
         #html.Div(id = 'put-graph-here',className='col-md-10'),
         dcc.Graph(id = 'my-graph'),
     ],className='row')

    ],className='container')
'''
@app.callback(Output('put-graph-here','children'),
              [Input('click-me','n_clicks')])
def draw_graph(n_clicks):
    
    data = ''
    if n_clicks > 0:

       data = dcc.Graph(
           id = 'my-graph',
           figure = {
               'data':go.Scatter(
                   x = np.arange(0,60),
                   y = np.random.randint(0,100),
                   type = 'Scatter',
                   mode = 'lines+markers'
                   ),
               'layout':go.Layout(title = 'My-graph')
               })
    
    
    return dcc.Graph(id = 'my-graph')

   '''     

my_css_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'

app.css.append_css({
    'external_url': my_css_url
    })

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8080)

