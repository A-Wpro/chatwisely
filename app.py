from dash import Dash, dcc, html,Output,Input
import os

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Server-Side Render External Website with Selenium"),
    html.Div(id="website-content")
])

if __name__ == '__main__':
  app.run_server(debug = False)

