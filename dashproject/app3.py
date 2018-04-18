import dash
from dash.dependencies import Output,Input,Event,State
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from mongoGuest import mongoGuest
from dockerGuest import dockerGuest
import random
docker=dockerGuest()
mongo = mongoGuest()
app = dash.Dash(__name__)

#---------------CSS Styling------------#

table_style = {
    'borderCollapse':'collapse',
    'width':'100%',
    'fontSize':'20px'
    
    }
tableh_style = {
    'border':'1px solid #dddddd',
    'padding':'8px',
    'backgroundColor':'#F2F2F2',
    }
tabled_style = {
    'border':'1px solid #dddddd',
    'padding':'8px',
    }

#-------------------------------------#


#------------APP Layout-------------------------------------------#
def generate_table():
    
    return html.Table(
      [html.Tr([html.Th('Id'),html.Th('Image'),html.Th('IPAddress'),html.Th('Gateway')],style=tableh_style)]+
[html.Tr([dcc.Link(html.Td(con['Id']),href=con['Id']),html.Td(con['Image']),html.Td(con['IPAddress']),html.Td(con['Gateway'])],
         style=tabled_style) for con in docker.get_cont_list()],className='table table-bordered',style=table_style     
    )

def serve_layout():
    
    return html.Div([
        html.Div([
        dcc.Location(id='url',refresh=False),
        html.Div([
            html.H2('Containers',style={'color':'#FFFFFF'}),
            ],className='row',style={'textAlign':'center','backgroundColor':'#000000'}),
        html.Div([
               generate_table()
            ],className='row'),
        ],id='index-page'),

        html.Div([
            html.Div([
            html.Div([
                dcc.Graph(id='cpu-usage-graph'),
                ],id='cpu-usage',className='col-md-6'),

            html.Div([
                dcc.Graph(id='memory-usage-graph'),
            ],id='memory-usage',className='col-md-6')
                ],className='row'),
            ],id='graph-page',style={'display':'none'}),      
    ],className='container')

app.layout = serve_layout

#---------------------------------------------------------#

@app.callback(Output('index-page','style'),
              [Input('url','pathname')])
def vanish(pathname):
    if len(pathname) > 1:
        return {'display':'none'}

@app.callback(Output('graph-page','style'),
              [Input('url','pathname')])
def appear(pathname):
    if len(pathname)>1:
        return {'display':'block'}

#------CPU Usage Graph generating callback-----------------#

def generate_cpu_data(cont_id):
    return mongo.get_cpu_usage(cont_id)
    
@app.callback(Output('cpu-usage-graph','figure'),
              [Input('url','pathname')])
def show_cpu_usage_graph(pathname):
    if len(pathname):
        X,Y = generate_cpu_data(pathname[1:])
        data = go.Scatter(
            x = X,
            y = Y,
            name='Scatter',
            mode='lines+markers'
            )
        layout = go.Layout(
            xaxis={'title':'Time','range':[min(X),max(X)]},
            yaxis={'title':'CPU','range':[min(Y),max(Y)]},
            )
        return {'data':[data],'layout':layout}
#----------------------------------------------


#------Memory Usage Graph Generating Callback------#
def generate_memory_data(cont_id):
    return mongo.get_memory_usage(cont_id)

@app.callback(Output('memory-usage-graph','figure'),
              [Input('url','pathname')])
def show_memory_usage_graph(pathname):
    if len(pathname)>1:
        X,Y = generate_memory_data(pathname[1:])
        data = go.Scatter(
            x = X,
            y = Y,
            name='Scatter',
            mode='lines+markers'
            )
        layout= go.Layout(
            xaxis = {'title':'Time','range':[min(X),max(X)]},
            yaxis = {'title':'Memory','range':[min(Y),max(Y)]},
            )
        return {'data':[data],'layout':layout}

#---------------------------------------------



#---------------Bootstrap CSS-------------------#

my_css_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
app.css.append_css({
    "external_url":my_css_url
    })

#------------------------------------------------#


if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8080)

