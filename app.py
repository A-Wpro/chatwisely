from dash import Dash, dcc, html

app = Dash(__name__)
server = app.server
layout = html.Div([
    html.H1('Load Another Webpage'),
    dcc.Input(id='url', type='text', placeholder='Enter a URL'),
    html.Button('Load Webpage', id='load-webpage'),
    html.Div(id='webpage-container'),
])

@app.callback(
    Output('webpage-container', 'children'),
    [Input('load-webpage', 'n_clicks')],
    [State('url', 'value')],
)
def load_webpage(n_clicks, url):
    if n_clicks is None or n_clicks == 0:
        return None

    iframe = html.Iframe(src=url, style={'width': '100%', 'height': '500px'})
    return iframe

if __name__ == '__main__':
  app.run_server(debug = False)
