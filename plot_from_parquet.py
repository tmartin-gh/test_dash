import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_parquet('data.parquet')

app.layout = html.Div([
    html.Div([
       html.Div([
           html.H3('Column 1'),
           dcc.Graph(
               id='time-vs-sinr',
               figure={
                   'data': [
                       go.Scatter(
                          x=df['t_sec'],
                          y=df['sinr_dB'],
                          name='SINR'
                       ),
                       go.Scatter(
                          x=df['t_sec'],
                          y=df['sinr_dB']+10,
                          name='Offset SINR'
                       )
                   ],
                   'layout': go.Layout(
                       xaxis={'type': 'linear', 'title': 'Time (seconds)'},
                       yaxis={'title': 'SINR (dB)'},
                       hovermode='closest'
                   )
               }
           )
       ], className='six columns'),

       html.Div([
          html.H3('Column 2'),
          dcc.Graph(
              id='sinr-histogram',
              figure={
                  'data': [
                      go.Histogram(
                         x=df['sinr_dB'],
                         histnorm='probability'
                      )
                  ],
                  'layout': go.Layout(
                      xaxis={'type': 'linear', 'title': 'SINR (dB)'},
                      yaxis={'title': 'Probability'},
                      hovermode='closest'
                  )
              }
          )
       ], className='six columns'),
    ], className='row'),

    html.Div([
       dcc.Graph(
           id='time-vs-bigNum',
           figure={
               'data': [
                   go.Scatter(
                      x=df['t_sec'],
                      y=np.log2(df['bigNum']),
                   )
               ],
               'layout': go.Layout(
                   xaxis={'type': 'linear', 'title': 'Time (seconds)'},
                   yaxis={'title': 'bigNum (# bits)'},
                   hovermode='closest'
               )
           }
       )
   ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
