import dash
from dash.dependencies import Output,Input,Event,State
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dockerGuest import dockerGuest
import random
docker=dockerGuest()
app = dash.Dash(__name__)

#image_list = docker.image_list()


#----------------APP LAYOUT------------------#

app.layout = html.Div([
     html.Div([
         html.Div([
         html.H3("Click below to see the list of containers"),
         html.Div([
                html.Button(id='generate-container-list',n_clicks=0,children='Show Containers',className='btn btn-primary')
             ],style={'marginTop':'30px'}),
       
         html.Div([
               html.P(children=[
                   html.H3(['Containers: ',
                            html.Span(id='list-length'),]),
               ]),
             ],id='div-list-length',style={'marginTop':'30px'}),

         html.Div([
             dcc.Dropdown(id='container-image-list',disabled=True),
             ]),
         ],className='left-row1'),

         html.Div([
              html.H3('Usages'),
              dcc.Dropdown(
                  id='usages',
                  options=[{'label':'CPU','value':'cpu_usage'},{'label':'Memory','value':'mem_usage'}],
              ),
             ],id='left-row-2',className='left-row2',style={'display':'none'}),
         ],className ='col-md-2',style={'backgroundColor':'#E6E6FA','marginLeft':'-65'}),
    
    html.Div(className='col-md-10'),
    ],className='container')

#---------------------------------------------#

@app.callback(Output('left-row-2','style'),
              [Input('generate-container-list','n_clicks')])
def update(n_clicks):
    l = len(docker.image_list())

    if n_clicks > 0:
        if l==0:
            return {'display':'none'}
        else:
            return {'display':'block'}


@app.callback(Output('container-image-list','disabled'),
              [Input('generate-container-list','n_clicks')])
def enable_dlist(n_clicks):
    l = len(docker.image_list())    
    if n_clicks>0:
        if l==0:
            return True
        else:
            return False

@app.callback(Output('list-length','children'),
              [Input('generate-container-list','n_clicks')])
def update(n_clicks):
    if n_clicks > 0:
        return '{}'.format(len(docker.image_list()))

@app.callback(Output('container-image-list','options'),
              [Input('generate-container-list','n_clicks')])
def generate_list(n_clicks): 
    if n_clicks > 0:
        return [{'label':i,'value':i} for i in docker.image_list()]

#---------------Bootstrap CSS-------------------#

my_css_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
app.css.append_css({
    "external_url":my_css_url
    })

#------------------------------------------------#


if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8888)

