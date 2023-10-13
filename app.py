from dash import Dash, dcc, html

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.Iframe(
        src='https://chat.openai.com/')
])

if __name__ == '__main__':
  app.run_server(debug = False)
