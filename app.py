from dash import Dash, dcc, html

app = Dash(__name__)
server = app.server
app.layout = html.Div("test---------")

  if __name__ == '__main__':
  app.run_server(debug = False)
