from dash import Dash, dcc, html

app = Dash(__name__)
server = app.server
layout = html.Div([
    dcc.Iframe(
        src='https://www.google.com',
        style={'width': '100%', 'height': '500px'}
    )
])

if __name__ == '__main__':
  app.run_server(debug = False)
