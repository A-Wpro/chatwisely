from dash import Dash, dcc, html,Output,Input
from selenium import webdriver
import os
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get("https://medium.com")
print(driver.page_source)
print("Finished!")

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
