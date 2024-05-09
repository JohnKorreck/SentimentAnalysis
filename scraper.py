from bs4 import BeautifulSoup

import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

def get_article_header_list(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/news'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.status_code)
        exit(1)
    print('Successful')

    soup = BeautifulSoup(response.content, 'html.parser')
    headline_links = soup.find_all('a', {'class': 'subtle-link fin-size-small titles noUnderline svelte-wdkn18'})
    headline_text = []
    for header in headline_links:
        headline_text.append(header.text)
    return headline_text

num = 1


tick = input('Enter a ticker: ')

for header in get_article_header_list(tick):
    print(f'{num}. ', header, '\n')
    num += 1
