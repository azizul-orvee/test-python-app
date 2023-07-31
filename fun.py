import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()

# Replace with the actual URLs of the pages you want to scrape
urls = [
    'https://circleci.com/docs/',
    'https://circleci.com/docs/2.0/',
    # Add more URLs as needed
]

for url in urls:
    content = scrape_page(url)
    with open(f'{url.replace("/", "_")}.html', 'w') as f:
        f.write(content)
