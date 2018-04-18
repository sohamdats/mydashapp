from dash.dependencies import Input,Output
import  dash_html_components as html
import dash_core_components as dcc

from app import app
from apps import app1,app2

def generate_table():

    return html.Table(
        [html.Tr([html.Th('Name'),html.Th('Roll')])]+

        [html.Tr([html.Td(dcc.Link('Soham Datta',href='soham')),html.Td('34512')])]+

        [html.Tr([html.Td(dcc.Link('Ricky Ponting',href='ricky')),html.Td('461678')])]
        )

app.layout = html.Div([
    dcc.Location(id='url',refresh=False),
    generate_table(),
    html.Div(id='page-content'),
    ])


@app.callback(Output('page-content','children'),
              [Input('url','pathname')])
def generate(pathname):
    return html.H3('My name is {}'.format(pathname[1:]))

if __name__ =='__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8080)




