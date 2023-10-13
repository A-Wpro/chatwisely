import dash
from dash import html
from selenium import webdriver

app = Dash(__name__)
server = app.server
@app.callback(
    dash.dependencies.Output("website-content", "children"),
    dash.dependencies.Input("fetch-button", "n_clicks")
)
def fetch_website(n_clicks):
    if n_clicks:
        # Set up a headless browser using Selenium
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        
        # Fetch the website
        browser.get("https://www.example.com")
        
        # Capture the page's final rendered HTML
        rendered_html = browser.page_source
        
        browser.quit()
        
        # Return the rendered HTML - though be cautious about security concerns!
        return html.Div(rendered_html, dangerouslySetInnerHTML={'__html': rendered_html})
    return ""

app.layout = html.Div([
    html.H1("Server-Side Render External Website with Selenium"),
    html.Button("Fetch Website Content", id="fetch-button"),
    html.Div(id="website-content")
])

if __name__ == '__main__':
  app.run_server(debug = False)
