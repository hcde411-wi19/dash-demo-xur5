
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# initialize Dash app and initialize the static folder

app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/data_car_2004.csv')

# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='2004 Car Data Scatter Plot'),

    # set the description underneath the heading
    html.Div(children='''
        Is there a Correlation between the Weight of a car and its Dealer Cost?
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # This is how we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"
                go.Scatter(
                    x=df['Weight'],
                    y=df['Dealer Cost'],
                    mode='markers',
                    text=df['Vehicle Name'],  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 8,
                        'opacity': 0.7  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                )
            ],
            'layout': {
                'title': 'Weight vs. Dealer Cost',
                # It is always a good practice to have axis labels.
                # This is especially important in this case as the numbers are not trivial
                'xaxis': {'title': 'Weight', 'range': [1000, 7000]},
                'yaxis': {'title': 'Dealer Cost', 'range': [0, 130000]},
                'height': 600
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)