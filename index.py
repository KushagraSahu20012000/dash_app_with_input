import dash
from dash import dcc, html, dash_table
from dash.dependencies import Output, Input, State
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import flask

server = flask.Flask(__name__)

input_df = pd.DataFrame()


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],server=server,
                    meta_tags=[{"name":"viewport", "content":"width=device-width"}])


input_df = pd.DataFrame()

global list_inputs
list_input = [0,0,0,input_df]
 

app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H6("Analysis Period:"),
                dcc.Input(id="anls_period_input",value=0)
            ],className="rounded-2 border-1 m-3 p-2 opacity-60",style={"backgroundColor" : "rgba(255,255,255,.7)","backdrop-filter":"blur(1px)"}),
            dbc.Col([
                html.H6("Market Rent:"),
                dcc.Input(id="market_rent_input",value=0)
            ],className="rounded-2 border-1 m-3 p-2 opacity-60",style={"backgroundColor" : "rgba(255,255,255,.7)","backdrop-filter":"blur(1px)"}),
            dbc.Col([
                html.H6("Capital Cost/SF:"),
                dcc.Input(id="capital_cost_input",value=0)
            ],className="rounded-2 border-1 m-3 p-2 opacity-60",style={"backgroundColor" : "rgba(255,255,255,.7)","backdrop-filter":"blur(1px)"}),

            
        ]),
        dbc.Row([
            html.Button(id='submit-button', n_clicks=0, children='Submit')
        ]),
        dbc.Row([
           dash_table.DataTable(
        id='table',
        columns=[
            {'id': 'col2', 'name': 'Name', 'type': 'text'},
            {'id': 'col3', 'name': 'Seats', 'type': 'numeric'},
            {'id': 'col4', 'name': 'SF/Seat', 'type': 'numeric'},
            {'id': 'col5', 'name': 'People', 'type': 'numeric'},
            {'id': 'col6', 'name': 'Vacancy', 'type': 'numeric'},
            {'id': 'col7', 'name': 'SF', 'type': 'text'},
            {'id': 'col8', 'name': 'Rent/SF', 'type': 'text'},
            {'id': 'col9', 'name': 'Annual Rent', 'type': 'text'}
        ],
        data=[
            { 'col2': '', 'col3': '', 'col4': '', 'col5': '', 'col6': '', 'col7': '', 'col8': '', 'col9': ''},
            {'col2': '', 'col3': '', 'col4': '', 'col5': '', 'col6': '', 'col7': '', 'col8': '', 'col9': ''},
            {'col2': '', 'col3': '', 'col4': '', 'col5': '', 'col6': '', 'col7': '', 'col8': '', 'col9': ''}
        ],
        editable=True,
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10
    )
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Checklist(["All","Random","LP"],inline = True,labelStyle = {'display': 'block', 'cursor': 'pointer',"margin-top":"10px", 'margin-right':'20px'})
                ],className="rounded-1 border-1 m-3 p-2 opacity-60")
        ]),
        dbc.Row(children=[
            html.P("",id="output-verify")
        ])
        ],fluid=True

)

@app.callback(
    Output("output-verify","children"),
    [Input("submit-button","n_clicks")],
    [State("anls_period_input","value"),State("market_rent_input","value"),State("capital_cost_input","value")]
)
def push(n_clicks,value1,value2,value3):
    list_input[0]=value1
    list_input[1] =value2
    list_input[2]=value3
    return str(list_input[0])+"  "+str(list_input[1])+"  "+str(list_input[2])


if __name__ == "__main__":
    app.run_server(debug=True,port=8000)

