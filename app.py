from dash import Dash, dcc, html,Output,Input
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
driver.get('http://www.google.com')
print('test')
driver.close()

app = Dash(__name__)
server = app.server
@app.callback(
    Output("website-content", "children"),
    Input("fetch-button", "n_clicks")
)
def fetch_website(n_clicks):
    if n_clicks:
        # Set up a headless browser using Selenium
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        
        # Fetch the website
        browser.get("https://chat.openai.com/")
        
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
