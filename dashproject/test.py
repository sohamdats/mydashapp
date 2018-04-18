import dash
from dash.dependencies import Output,Input,Event,State
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dockerGuest import dockerGuest
import random
docker=dockerGuest()
app = dash.Dash(__name__)

def generate_graph():
    
    return html.Table(
        [html.Tr([html.Th('Name'),html.Th('Roll')])]+
        [html.Tr([html.Td('Soham Datta'),html.Td('12345')])]+
        [html.Tr([html.Td('Ricky Ponting'),html.Td('5666')])]
    )


app.layout = html.Div([
   
        html.H4('This is a table'),
        generate_graph(),
    ],className='container')



#---------------Bootstrap CSS-------------------#

my_css_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
app.css.append_css({
    "external_url":my_css_url
    })

#------------------------------------------------#


if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8080)

